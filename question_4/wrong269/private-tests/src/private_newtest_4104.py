from wrong_4_269 import *

import pytest
@pytest.mark.timeout(5)
def test_4104():
    assert sort_age([('F', 20)]) == [('F', 20)]
