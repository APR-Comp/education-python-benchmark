from wrong_4_314 import *

import pytest
@pytest.mark.timeout(5)
def test_17691():
    assert sort_age([('M', 9)]) == [('M', 9)]
