from ipapi import get_location

def get_postal(): 
    return Postal(get_location())
def test_postal():
    assert get_postal() == 1811
