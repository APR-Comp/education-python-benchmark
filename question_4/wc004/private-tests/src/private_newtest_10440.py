from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_10440():
    assert sort_age([('F', 5), ('M', 4), ('F', 6), ('F', 3), ('M', 10), ('F', 21)]) == [('F', 21), ('M', 10), ('F', 6), ('F', 5), ('M', 4), ('F', 3)]
