from ipapi import get_location

def get_ip(): 
    return ip(get_location())

def test_ip():
    assert get_ip()