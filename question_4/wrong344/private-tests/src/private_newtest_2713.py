from wrong_4_344 import *

import pytest
@pytest.mark.timeout(5)
def test_2713():
    assert sort_age([('M', 23)]) == [('M', 23)]