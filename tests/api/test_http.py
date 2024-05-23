import pytest
import requests

@pytest.mark.http
def test_first_request():
    fr = requests.get('https://api.github.com/zen')
    print(f"Test1. Response from server is: {fr.text}")

@pytest.mark.http
def test_second_request():
    sr = requests.get('https://api.github.com/users/defunkt')
    body = sr.json()
    header = sr.headers

    print(f'Test2. Response from Server is: {sr.text}')
    print (f'Test2. STATUS_CODE is: {sr.status_code}')
    print(f'Test2. NAME is: {body['name']}')
    print(f'Test2. HEADER is: {header['Server']}')
    
    assert body['name'] == 'Chris Wanstrath'
    assert sr.status_code == 200
    assert header['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    stc = requests.get('https://api.github.com/users/viktoriya_katrych')
    print (f'Test3. STATUS_CODE is: {stc.status_code}')
    assert stc.status_code == 404  
 


    
