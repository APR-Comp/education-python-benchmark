from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_6517():
    assert remove_extras([52, 6]) == [52, 6]
