from wrong_correct_5_049 import *

import pytest
@pytest.mark.timeout(5)
def test_8209():
    assert top_k([253, 212, 856, 851],3) == [856, 851, 253]
