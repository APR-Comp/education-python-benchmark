from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_10566():
    assert remove_extras([22585, 775, 3, 42, 1, 9, 3, 738]) == [22585, 775, 3, 42, 1, 9, 738]
