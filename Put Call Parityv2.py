import scipy.stats as stats
import numpy as np

def black_scholes(S, X, T, r, sigma, option_type='call'):
    """
    Calculate European option price using Black-Scholes formula.

    Parameters:
    - S: Current stock price
    - X: Option strike price
    - T: Time to expiration (in years)
    - r: Risk-free rate
    - sigma: Volatility of the underlying stock
    - option_type: 'call' for call option, 'put' for put option

    Returns:
    - Option price
    """

    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * stats.norm.cdf(d1) - X * np.exp(-r * T) * stats.norm.cdf(d2)
    elif option_type == 'put':
        option_price = X * np.exp(-r * T) * stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price


# parameters
S = 100  # Current stock price
X = 100  # Option strike price
T = 1  # Time to expiration (in years)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

# Calculate call and put prices
call_price = black_scholes(S, X, T, r, sigma, option_type='call')
put_price = black_scholes(S, X, T, r, sigma, option_type='put')

# Verify Put-Call Parity
lhs = call_price - put_price
rhs = S - X * np.exp(-r * T)


print(lhs,rhs)