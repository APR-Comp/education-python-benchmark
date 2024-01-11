from wrong_4_294 import *

import pytest
@pytest.mark.timeout(5)
def test_15573():
    assert sort_age([('F', 8), ('M', 21)]) == [('M', 21), ('F', 8)]
