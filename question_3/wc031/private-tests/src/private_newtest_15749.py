from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_15749():
    assert remove_extras([6, 98, 7, 4, 86]) == [6, 98, 7, 4, 86]
