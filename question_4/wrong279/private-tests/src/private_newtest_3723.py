from wrong_4_279 import *

import pytest
@pytest.mark.timeout(5)
def test_3723():
    assert sort_age([('F', 3), ('F', 20)]) == [('F', 20), ('F', 3)]
