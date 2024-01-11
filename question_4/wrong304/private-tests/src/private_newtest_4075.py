from wrong_4_304 import *

import pytest
@pytest.mark.timeout(5)
def test_4075():
    assert sort_age([('M', 3)]) == [('M', 3)]
