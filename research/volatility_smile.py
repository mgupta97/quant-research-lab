import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pricing.implied_volatility import (
    implied_volatility,
)

S = 100
T = 1
r = 0.05

market_data = [
    (80, 24.59),
    (90, 16.70),
    (100, 10.45),
    (110, 6.04),
    (120, 3.25),
]

strikes = []
ivs = []

for K, market_price in market_data:
    iv = implied_volatility(
        market_price=market_price,
        S=S,
        K=K,
        T=T,
        r=r,
        option_type="call",
    )

    strikes.append(K)
    ivs.append(iv)

    print(
        f"Strike={K}, IV={iv:.4f}"
    )

plt.figure(figsize=(10, 6))

plt.plot(
    strikes,
    ivs,
    marker="o",
)

plt.title("Volatility Smile")
plt.xlabel("Strike")
plt.ylabel("Implied Volatility")

plt.grid(True)

output_dir = Path("research/figures")
output_dir.mkdir(
    parents=True,
    exist_ok=True,
)

plt.savefig(
    output_dir / "volatility_smile.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
