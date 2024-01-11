from wrong_3_289 import *

import pytest
@pytest.mark.timeout(5)
def test_18335():
    assert remove_extras([11]) == [11]
