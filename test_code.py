from ipapi import get_location

def get_length(): 
    return len(get_location())

def test_length(): 
    assert get_length() == 9

def test_null(): 
    for i in get_location(): #test
        assert i != None