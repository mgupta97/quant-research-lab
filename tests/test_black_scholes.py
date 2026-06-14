from src.pricing.black_scholes import call_price

def test_call_price():
    price = call_price(S=100, K=100, T=1, r=0.05, sigma=0.2)
    
    assert round(price, 2) == 10.45
