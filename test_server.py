import requests as req

def test_200_ok_status_home_route():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_response_body_home_route():
    response = req.get('http://127.0.0.1:5000')
    assert b'Welcome to my site' in response.content


def test_404_not_found_status():
    response = req.get('http://127.0.0.1:5000/heyyyyy')
    assert response.status_code == 404


