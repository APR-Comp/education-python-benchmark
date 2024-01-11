from wrong_4_294 import *

import pytest
@pytest.mark.timeout(5)
def test_10992():
    assert sort_age([('M', 7), ('F', 9)]) == [('F', 9), ('M', 7)]
