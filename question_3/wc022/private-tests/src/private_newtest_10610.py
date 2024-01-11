from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_10610():
    assert remove_extras([163, 8]) == [163, 8]
