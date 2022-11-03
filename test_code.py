from ipapi import get_location

def get_postal(): 
    return Postal(get_location())
