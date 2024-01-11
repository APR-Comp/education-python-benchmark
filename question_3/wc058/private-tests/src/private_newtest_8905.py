from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_8905():
    assert remove_extras([97, 3]) == [97, 3]
