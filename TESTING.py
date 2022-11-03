from Option2_Project import get_location

def get_postal():
    return pos(get_location())

def test_postal():
    assert  get_postal()


