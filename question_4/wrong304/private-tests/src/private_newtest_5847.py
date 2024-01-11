from wrong_4_304 import *

import pytest
@pytest.mark.timeout(5)
def test_5847():
    assert sort_age([('M', 32)]) == [('M', 32)]
