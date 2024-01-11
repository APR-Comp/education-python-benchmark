from wrong_4_304 import *

import pytest
@pytest.mark.timeout(5)
def test_1413():
    assert sort_age([('F', 26)]) == [('F', 26)]
