from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_8133():
    assert sort_age([('M', 5), ('F', 8), ('F', 18), ('F', 2)]) == [('F', 18), ('F', 8), ('M', 5), ('F', 2)]
