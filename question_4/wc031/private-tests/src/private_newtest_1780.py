from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_1780():
    assert sort_age([('F', 27), ('F', 6), ('M', 5)]) == [('F', 27), ('F', 6), ('M', 5)]
