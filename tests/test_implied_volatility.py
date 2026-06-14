from src.pricing.black_scholes import call_price
from src.pricing.implied_volatility import implied_volatility

def test_call_implied_volatility():
    market_price = call_price(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
    )

    estimated_sigma = implied_volatility(
        market_price = market_price,
        S= 100,
        K = 100, 
        T=1, 
        r=0.05,
        option_type="call",
        )
    
    assert round(estimated_sigma, 4) == 0.2

