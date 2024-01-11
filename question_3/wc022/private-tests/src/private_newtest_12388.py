from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_12388():
    assert remove_extras([77]) == [77]
