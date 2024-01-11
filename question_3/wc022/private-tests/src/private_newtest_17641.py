from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_17641():
    assert remove_extras([3, 7, 8, 48]) == [3, 7, 8, 48]
