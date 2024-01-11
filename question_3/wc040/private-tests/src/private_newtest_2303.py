from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_2303():
    assert remove_extras([5, 72]) == [5, 72]
