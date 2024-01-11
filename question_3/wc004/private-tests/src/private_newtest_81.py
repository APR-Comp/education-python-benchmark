from wrong_correct_3_004 import *

import pytest
@pytest.mark.timeout(5)
def test_81():
    assert remove_extras([2, 7, 57]) == [2, 7, 57]
