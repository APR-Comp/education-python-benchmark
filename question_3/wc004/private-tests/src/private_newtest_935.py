from wrong_correct_3_004 import *

import pytest
@pytest.mark.timeout(5)
def test_935():
    assert remove_extras([52, 98]) == [52, 98]
