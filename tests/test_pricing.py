import numpy as np

from black_scholes import call_price,put_price
from monte_carlo import monte_carlo_call_price_crn,monte_carlo_put_price_crn

S_0 = 100
r = 0.05
sigma = 0.2
T = 1
K=100

def test_put_call_parity():
    call = call_price(S_0, r, sigma, T,K)
    put = put_price(S_0, r, sigma, T,K)
    lhs = call - put
    rhs = S_0 - K * np.exp(-r * T)
    assert abs(lhs - rhs) < 1e-10
def test_monte_carlo_call_close_to_black_scholes():
    np.random.seed(42)
    N = 100000
    mc_price = monte_carlo_call_price_crn(S_0,r, sigma, T,K, N)
    bs_price = call_price(S_0, r, sigma, T,K)
    assert abs(mc_price - bs_price) < 0.1
def test_monte_carlo_put_close_to_black_scholes():
    np.random.seed(42)
    N = 100000
    mc_price = monte_carlo_put_price_crn(S_0,r, sigma, T,K, N)
    bs_price = put_price(S_0, r, sigma, T,K)
    assert abs(mc_price - bs_price) < 0.1



