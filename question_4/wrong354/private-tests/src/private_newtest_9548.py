from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_9548():
    assert sort_age([('M', 30)]) == [('M', 30)]
