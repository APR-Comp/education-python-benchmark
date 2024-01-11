from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_7839():
    assert sort_age([('F', 0), ('F', 1), ('M', 7)]) == [('M', 7), ('F', 1), ('F', 0)]
