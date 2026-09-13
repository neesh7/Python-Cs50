from calculator import square
import pytest
# breaking testing into diff categories

def test_zero_sq():
    assert square(0) == 0

def test_postiive_sq():
    assert square(2) == 4
    assert square(11) == 121

def test_negative_sq():
    assert square(-5) == 25
    assert square(-9) == 81

def test_str():
    with pytest.raises(TypeError):
        square("cat")