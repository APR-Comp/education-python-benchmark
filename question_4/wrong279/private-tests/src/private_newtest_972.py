from wrong_4_279 import *

import pytest
@pytest.mark.timeout(5)
def test_972():
    assert sort_age([('F', 1)]) == [('F', 1)]