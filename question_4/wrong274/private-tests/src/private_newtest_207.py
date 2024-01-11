from wrong_4_274 import *

import pytest
@pytest.mark.timeout(5)
def test_207():
    assert sort_age([('M', 28), ('M', 9), ('M', 4)]) == [('M', 28), ('M', 9), ('M', 4)]
