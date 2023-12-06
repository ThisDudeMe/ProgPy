import pytest
from app.math import divide

def test_div_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

