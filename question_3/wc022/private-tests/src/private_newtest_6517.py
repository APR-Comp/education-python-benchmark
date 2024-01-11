from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_6517():
    assert remove_extras([52, 6]) == [52, 6]
