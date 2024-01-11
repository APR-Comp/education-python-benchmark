from wrong_4_269 import *

import pytest
@pytest.mark.timeout(5)
def test_7558():
    assert sort_age([('F', 19), ('F', 8)]) == [('F', 19), ('F', 8)]
