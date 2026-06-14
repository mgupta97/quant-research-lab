import sys 
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pricing.black_scholes import vega

S= 100
T = 1
r = 0.05            
sigma = 0.20

strikes = list(range(60, 145, 5))

vega_values = [vega(S, K, T, r, sigma) for K in strikes]

max_vega = max(vega_values)
max_strike = strikes[vega_values.index(max_vega)]

plt.figure(figsize=(10, 6))
plt.plot(strikes, vega_values, marker='o')
plt.axvline(max_strike, linestyle="--", label = f"Max Vega Strike: {max_strike}")
plt.title("Vega Across Strike Prices")
plt.xlabel("Strike Price")
plt.ylabel("Vega")
plt.legend()
plt.grid(True)

output_dir = Path("research/figures")
output_dir.mkdir(parents=True, exist_ok = True)

plt.savefig(output_dir / "vega_across_strikes.png", dpi= 300, bbox_inches="tight")
plt.show()

print(f"Maximum Vega: {max_vega:.4f}")
print(f"Strike with Maximum Vega: {max_strike}")

