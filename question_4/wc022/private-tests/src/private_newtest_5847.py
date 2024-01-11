from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_5847():
    assert sort_age([('M', 32)]) == [('M', 32)]
