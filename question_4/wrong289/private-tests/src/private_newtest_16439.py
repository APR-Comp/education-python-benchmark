from wrong_4_289 import *

import pytest
@pytest.mark.timeout(5)
def test_16439():
    assert sort_age([('M', 17)]) == [('M', 17)]
