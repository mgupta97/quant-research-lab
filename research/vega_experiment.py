import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pricing.black_scholes import vega

S= 100
T = 1
r = 0.05            
sigma = 0.20

strikes = [90, 95, 100, 105, 110, 115, 120]

for K in strikes:
    value = vega(S, K, T, r, sigma)
    print(f"Strike= {K}, Vega = {value:.4f}")

