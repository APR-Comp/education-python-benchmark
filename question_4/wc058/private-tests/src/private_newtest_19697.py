from wrong_correct_4_058 import *

import pytest
@pytest.mark.timeout(5)
def test_19697():
    assert sort_age([('F', 23)]) == [('F', 23)]
