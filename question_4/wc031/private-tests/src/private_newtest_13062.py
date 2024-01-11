from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_13062():
    assert sort_age([('M', 5)]) == [('M', 5)]
