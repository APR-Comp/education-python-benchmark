from wrong_correct_3_013 import *

import pytest
@pytest.mark.timeout(5)
def test_14624():
    assert remove_extras([2]) == [2]