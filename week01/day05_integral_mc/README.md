# Day 05 — Monte Carlo estimation of an integral

## Idea
We estimate a definite integral by interpreting it as an expectation and approximating it
via Monte Carlo sampling.

## Problem
Estimate the integral
\[
\int_0^1 x^2 \, dx
\]
whose exact value is \(1/3\).

## Monte Carlo estimator
Let \(X_1, \dots, X_N \sim \mathrm{Uniform}(0,1)\).  
The Monte Carlo estimator is
\[
\hat{I}_N = \frac{1}{N} \sum_{i=1}^N X_i^2.
\]

## Running convergence
The script prints the running estimate \(\hat{I}_k\) every `step` iterations together with
an error scale
\[
\mathrm{err} \sim \frac{1}{\sqrt{k}}.
\]

## How to run
```bash
python integral_mc.py
