from wrong_4_349 import *

import pytest
@pytest.mark.timeout(5)
def test_1147():
    assert sort_age([('M', 1), ('M', 13), ('F', 30)]) == [('F', 30), ('M', 13), ('M', 1)]
