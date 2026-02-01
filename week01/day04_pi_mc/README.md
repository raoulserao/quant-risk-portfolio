# Day 04 — Monte Carlo estimation of π

## Idea
We sample points uniformly in the square \([-1,1]^2\) and count how many fall inside the unit circle.
The area ratio yields an estimator of π.

## Estimator
Let \(S\) be the number of points inside the circle out of \(N\) total points:
\[
\hat{\pi} = 4 \frac{S}{N}
\]

## Running convergence
The script prints the running estimate \(\hat{\pi}_k\) every `step` iterations, together with an error scale:
\[
\text{err} \sim \frac{4}{\sqrt{k}}
\]
This `err` is an order-of-magnitude scale (not a strict bound).

## How to run
```bash
python pi_mc.py
