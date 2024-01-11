from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_1261():
    assert remove_extras([8283, 67, 827, 9, 5493441, 2, 9, 8, 16]) == [8283, 67, 827, 9, 5493441, 2, 8, 16]
