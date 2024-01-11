from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_12646():
    assert sort_age([('F', 7), ('F', 35)]) == [('F', 35), ('F', 7)]
