def test_api():
    import requests
    assert requests.get('http://localhost:8000/').status_code == 200