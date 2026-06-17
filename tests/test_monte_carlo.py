from src.pricing.black_scholes import call_price
from src.pricing.monte_carlo import monte_carlo_call_price


def test_monte_carlo_call_price_close_to_black_scholes():
    bs_price = call_price(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
    )

    mc_price = monte_carlo_call_price(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        num_simulations=100_000,
        seed=42,
    )

    assert abs(mc_price - bs_price) < 0.15