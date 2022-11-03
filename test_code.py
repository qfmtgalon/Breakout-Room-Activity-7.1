from ipapi import get_location

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_ip(): 
    return ip(get_location())

def test_ip():
    assert get_ip()