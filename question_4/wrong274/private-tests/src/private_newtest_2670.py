from wrong_4_274 import *

import pytest
@pytest.mark.timeout(5)
def test_2670():
    assert sort_age([('F', 28), ('M', 13)]) == [('F', 28), ('M', 13)]
