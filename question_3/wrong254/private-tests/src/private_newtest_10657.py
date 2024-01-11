from wrong_3_254 import *

import pytest
@pytest.mark.timeout(5)
def test_10657():
    assert remove_extras([587]) == [587]
