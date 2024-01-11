from wrong_correct_1_022 import *

import pytest
@pytest.mark.timeout(5)
def test_4717():
    assert search(64,[4, 8, 29514]) == 2
