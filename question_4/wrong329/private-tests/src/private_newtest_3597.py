from wrong_4_329 import *

import pytest
@pytest.mark.timeout(5)
def test_3597():
    assert sort_age([('F', 2), ('F', 3), ('M', 21)]) == [('M', 21), ('F', 3), ('F', 2)]
