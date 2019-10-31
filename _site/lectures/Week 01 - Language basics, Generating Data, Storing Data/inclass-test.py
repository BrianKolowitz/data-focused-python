

def test_add_two_params():
    expected = 5
    actual = add(2, 3)
    assert expected == actual

def test_add_three_params():
    expected = 9
    actual = add(2, 3, 4)
    assert expected == actual

def add(a, b, c=None):
    if c is None:
        return a + b
    else:
        return a + b + c