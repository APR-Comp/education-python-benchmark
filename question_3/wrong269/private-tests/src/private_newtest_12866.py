from wrong_3_269 import *

import pytest
@pytest.mark.timeout(5)
def test_12866():
    assert remove_extras([5, 56, 41]) == [5, 56, 41]
