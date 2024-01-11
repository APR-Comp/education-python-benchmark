from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_10215():
    assert sort_age([('F', 7)]) == [('F', 7)]
