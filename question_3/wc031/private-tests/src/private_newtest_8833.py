from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_8833():
    assert remove_extras([8]) == [8]
