from wrong_correct_4_004 import *

import pytest
@pytest.mark.timeout(5)
def test_7184():
    assert sort_age([('F', 26)]) == [('F', 26)]