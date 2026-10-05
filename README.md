# Monte Carlo Option Pricing

A Python implementation of Monte Carlo methods for pricing European options
under the Black-Scholes model.

The project compares simulation-based prices and Greeks with analytical
Black-Scholes results, while investigating convergence, confidence intervals,
variance reduction and finite-difference methods.

## Objectives

- Implement a Monte Carlo European call and put pricer
- Compare Monte Carlo prices with Black-Scholes analytical prices
- Investigate convergence as the number of simulations increases
- Quantify Monte Carlo uncertainty using confidence intervals
- Implement antithetic variates for variance reduction
- Estimate Delta, Gamma and Vega using finite differences
- Use common random numbers to reduce the variance of Greek estimates
- Investigate the effect of finite-difference step size on Gamma

## Methods

The project will use:

* Python
* NumPy
* Pandas
* Matplotlib

## Mathematical Model

Under the risk-neutral Black-Scholes model, the terminal stock price is

$$
S_T = S_0 \exp\left[
\left(r-\frac{1}{2}\sigma^2\right)T
+\sigma\sqrt{T}Z
\right],
\qquad Z\sim N(0,1).
$$

For a European call, the Monte Carlo estimator is

$$
\hat{C}=
e^{-rT}\frac{1}{N}
\sum_{i=1}^{N}
\max(S_T^{(i)}-K,0).
$$

The standard error is

$$
SE=e^{-rT}\frac{s}{\sqrt{N}},
$$

where $s$ is the sample standard deviation of the simulated payoffs.

A 95% confidence interval is approximately

$$
\hat{C}\pm1.96SE.
$$

## Greeks

The project estimates the Greeks using finite differences.

### Delta

$$
\Delta \approx
\frac{C(S_0+h)-C(S_0-h)}{2h}
$$

### Gamma

$$
\Gamma \approx
\frac{C(S_0+h)-2C(S_0)+C(S_0-h)}{h^2}
$$

### Vega

$$
\nu \approx
\frac{C(\sigma+h)-C(\sigma-h)}{2h}
$$

Common random numbers are used for the finite-difference calculations so
that the same underlying random shocks are used for the perturbed prices.

## Variance Reduction

Antithetic variates were investigated as a variance-reduction technique.

Common random numbers were also tested when estimating Delta. In the
experiment, the standard deviation of the Delta estimator decreased from

$$
0.03193
$$

with independent random numbers to

$$
0.00178
$$

using common random numbers.

This represents an approximately 94% reduction in standard deviation.

## Finite-Difference Step Size

The Gamma estimator was evaluated for several finite-difference step sizes.
The results demonstrated a trade-off between finite-difference approximation
error and Monte Carlo noise.

As the step size becomes very small, the $1/h^2$ scaling in the Gamma
estimator amplifies simulation noise.

## Project Structure

``` text
├── src/
│   ├── black_scholes.py
│   └── monte_carlo.py
│   └── antithetic.py
│
├── tests/
│   └── test_pricing.py
│
├── notebooks/
│   └── Option_Pricing_Analysis.ipynb
│
├── .gitignore
└── README.md
