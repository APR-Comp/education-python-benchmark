from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_338():
    assert sort_age([('M', 12)]) == [('M', 12)]
