from wrong_4_314 import *

import pytest
@pytest.mark.timeout(5)
def test_17092():
    assert sort_age([('M', 15)]) == [('M', 15)]
