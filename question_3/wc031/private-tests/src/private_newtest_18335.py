from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_18335():
    assert remove_extras([11]) == [11]
