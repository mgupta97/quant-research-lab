from src.pricing.black_scholes import call_price, put_price, call_delta, put_delta, gamma

def test_call_price():
    price = call_price(S=100, K=100, T=1, r=0.05, sigma=0.2)
    
    assert round(price, 2) == 10.45

def test_put_price():
    price = put_price(S=100, K=100, T=1, r=0.05, sigma=0.2)

    assert round(price, 2) == 5.57

def test_call_delta():
    delta = call_delta(S=100, K=100, T=1, r=0.05, sigma=0.2)

    assert round(delta, 2) == 0.64

def test_put_delta():
    delta = put_delta(S=100, K=100, T=1, r=0.05, sigma=0.2)

    assert round(delta, 2) == -0.36

def test_gamma():
    gamma_value = gamma(S=100, K=100, T=1, r=0.05, sigma=0.2)

    assert round(gamma_value, 4) == 0.0188