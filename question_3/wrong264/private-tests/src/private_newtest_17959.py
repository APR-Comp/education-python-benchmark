from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_17959():
    assert remove_extras([3]) == [3]
