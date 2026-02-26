# Monte Carlo Comparison of Investment Strategies

This project performs a Monte Carlo simulation comparing three investment strategies over a 5-year horizon (60 months).

## Strategies

1. **Threshold trading strategy**
   - Buy when the price falls below a lower threshold.
   - Sell when the price rises above an upper threshold.
   - Cash earns a fixed monthly interest rate.

2. **Buy & Hold**
   - Invest the full capital at time 0.
   - Hold the position until the end of the horizon.

3. **Savings Only**
   - Keep the capital in cash.
   - Earn a fixed monthly interest rate.

---

## Price Process

The underlying price follows a discrete stochastic process:

- 50% probability: no change
- 25% probability: +5%
- 25% probability: −5%

This process has:
- Zero arithmetic expected return per step
- Negative geometric (log) growth

---

## Methodology

- Parameters are defined at the top of the script.
- Monte Carlo simulation with 10,000 paths.
- Portfolio value is computed at each time step.
- Final portfolio values are stored for each strategy.
- Statistics computed:
  - Mean
  - Median
  - Minimum
  - Maximum
- Visualization:
  - Average portfolio path
  - Distribution of final portfolio values

---

## Key Observations

- **Buy & Hold** shows a right-skewed distribution:
  - The mean is close to the initial capital.
  - The median is lower due to negative log-growth.
  - Rare but large positive outcomes increase the maximum significantly.

- **Savings Only** produces a deterministic outcome:
  - Final value is fixed and equal across all simulations.

- **Threshold Strategy** modifies the distribution:
  - It reduces extreme positive outcomes.
  - It also reduces exposure to prolonged downturns.
  - The average outcome lies between Buy & Hold and Savings.

This illustrates how nonlinear trading rules alter the distribution of outcomes compared to passive strategies.

---

## Purpose of the Project

The goal of this project is to:

- Understand path dependency in stochastic processes.
- Compare mean vs median behavior.
- Observe the difference between arithmetic and geometric growth.
- Study how simple trading rules reshape risk and return profiles.
