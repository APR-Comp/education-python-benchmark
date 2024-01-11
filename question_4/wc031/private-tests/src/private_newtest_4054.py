from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_4054():
    assert sort_age([('F', 12)]) == [('F', 12)]
