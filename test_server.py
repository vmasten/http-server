import requests as req


# GET routes


def test_200_ok_status_home_route():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_response_body_home_route():
    response = req.get('http://127.0.0.1:5000')
    assert b'cowsay' in response.content


def test_invalid_method_home_route():
    response = req.post('http://127.0.0.1:5000')
    assert response.status_code == 400


def test_200_ok_status_get_cow_route():
    msg = 'hello'
    response = req.get(f'http://127.0.0.1:5000/cow?msg={msg}')
    assert response.status_code == 200


def test_response_body_get_cow_route():
    msg = 'hello'
    response = req.get(f'http://127.0.0.1:5000/cow?msg={msg}')
    assert b'hello' in response.content


def test_no_params_get_cow_route():
    response = req.get('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_400_bad_request_get_cow_route():
    response = req.get(f'http://127.0.0.1:5000/cow?who=dat&wat=do')
    assert response.status_code == 400


def test_invalid_method_get_cow_route():
    msg = 'hello'
    response = req.put(f'http://127.0.0.1:5000/cow?msg={msg}')
    assert response.status_code == 405


# POST routes


def test_201_created_status_post_cow_route():
    msg = 'hello'
    response = req.post(f'http://127.0.0.1:5000/cow?msg={msg}')
    assert response.status_code == 201


def test_no_params_post_cow_route():
    response = req.post('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_400_bad_request_post_cow_route():
    response = req.post(f'http://127.0.0.1:5000/cow?who=dat&wat=do')
    assert response.status_code == 400


def test_invalid_method_post_cow_route():
    msg = 'hello'
    response = req.head(f'http://127.0.0.1:5000/cow?msg={msg}')
    assert response.status_code == 405


# 404


def test_404_not_found_status():
    response = req.get('http://127.0.0.1:5000/heyyyyy')
    assert response.status_code == 404
