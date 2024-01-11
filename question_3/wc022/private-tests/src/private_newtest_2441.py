from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_2441():
    assert remove_extras([26, 55938, 1]) == [26, 55938, 1]
