from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_19516():
    assert sort_age([('M', 7), ('M', 8), ('F', 9), ('F', 4)]) == [('F', 9), ('M', 8), ('M', 7), ('F', 4)]
