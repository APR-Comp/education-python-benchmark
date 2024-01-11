from wrong_4_324 import *

import pytest
@pytest.mark.timeout(5)
def test_8109():
    assert sort_age([('M', 18), ('F', 1), ('M', 7), ('F', 2), ('M', 9)]) == [('M', 18), ('M', 9), ('M', 7), ('F', 2), ('F', 1)]
