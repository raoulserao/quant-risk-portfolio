import numpy as np
import matplotlib.pyplot as plt

#Parameters
T = 60
N = 10000
p_flat = 0.5
p_up = 0.25
up_move = 0.05
down_move = -0.05
interest = 0.005
cash0=1000
price0=100
buy_th=95
sell_th=110
shares2=cash0/price0


final_final_values = np.zeros((N, 3))
paths1=np.zeros((N,T+1))
paths2=np.zeros((N,T+1))
paths3=np.zeros((N,T+1))

rng = np.random.default_rng(42)



for sim in range(N):
    price = price0
    cash = cash0
    shares = 0.0

    paths1[sim, 0] = cash  # initial value portfolio strategy 1
    paths2[sim, 0] = cash  # initial value portfolio strategy 2
    paths3[sim, 0] = cash  # initial value portfolio strategy 3
    u = rng.random(T)
    #first strategy: threshold
    for t, x in enumerate(u, start=1):
        # 1) price evolution: flat 1/2, up 1/4, down 1/4
        if x < p_flat:
            pass
        elif x < p_flat+ p_up:
            price *= (1+up_move)
        else:
            price *= (1+down_move)

        # 2) buy/sell strategy
        if price < buy_th and cash > 0:
            shares = cash / price
            cash = 0.0
        elif price > sell_th and shares > 0:
            cash = shares * price
            shares = 0.0

        # 3) cash interest (applied only when in cash)
        if cash > 0:
            cash *= (1 + interest)

        #Portfolio value at time t
        portfolio1 = cash + shares * price
        paths1[sim, t] = portfolio1

    #second strategy: buy&hold
        portfolio2=shares2*price
        paths2[sim,t]=portfolio2

    #third strategy: savings only
        portfolio3 = cash0 * (1 + interest)**t
        paths3[sim, t] = portfolio3
    
    final_final_values[sim]=np.array([paths1[sim,-1],paths2[sim,-1],paths3[sim,-1]])

# --- statistics ---
print("Final mean:", final_final_values.mean(axis=0))
print("Final median:", np.median(final_final_values, axis=0))
print("Min:", final_final_values.min(axis=0))
print("Max:", final_final_values.max(axis=0))

# --- grafici ---
mean_path1 = paths1.mean(axis=0)
mean_path2 = paths2.mean(axis=0)
mean_path3 = paths3.mean(axis=0)

plt.figure()
plt.plot(mean_path1, label="Threshold strategy")
plt.plot(mean_path2, label="Buy & Hold")
plt.plot(mean_path3, label="Savings only")

plt.title("Average Portfolio Value (Monte Carlo)")
plt.xlabel("Months")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid(True)

plt.show()

plt.figure()
plt.hist(final_final_values[:,0], bins=30, alpha=0.5, label="Threshold")
plt.hist(final_final_values[:,1], bins=30, alpha=0.5, label="Buy & Hold")
plt.hist(final_final_values[:,2], bins=30, alpha=0.5, label="Savings")
plt.legend()
plt.title("Final value distribution")
plt.xlabel("Final value")
plt.ylabel("Frequency")
plt.show()
