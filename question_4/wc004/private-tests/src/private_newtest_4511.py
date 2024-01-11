from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_4511():
    assert sort_age([('M', 12), ('F', 2), ('F', 9), ('F', 10)]) == [('M', 12), ('F', 10), ('F', 9), ('F', 2)]
