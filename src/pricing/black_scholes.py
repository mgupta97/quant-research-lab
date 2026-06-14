import numpy as np 
from scipy.stats import norm 

def calculate_d1(S, K, T, r, sigma):
    numerator = np.log(S / K) + (r + 0.5 * sigma ** 2) * T
    denominator = sigma * np.sqrt(T)
    return numerator / denominator

def calculate_d2(d1, sigma, T):
    return d1 - sigma * np.sqrt(T)

def call_price(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    return (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))

def put_price(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    return (K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1))
