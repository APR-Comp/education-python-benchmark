from wrong_correct_4_058 import *

import pytest
@pytest.mark.timeout(5)
def test_13067():
    assert sort_age([('F', 6)]) == [('F', 6)]
