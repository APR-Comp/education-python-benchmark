from wrong_4_349 import *

import pytest
@pytest.mark.timeout(5)
def test_12962():
    assert sort_age([('F', 8), ('M', 4), ('M', 7), ('M', 36), ('M', 9)]) == [('M', 36), ('M', 9), ('F', 8), ('M', 7), ('M', 4)]
