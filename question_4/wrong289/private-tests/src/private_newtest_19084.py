from wrong_4_289 import *

import pytest
@pytest.mark.timeout(5)
def test_19084():
    assert sort_age([('F', 6)]) == [('F', 6)]
