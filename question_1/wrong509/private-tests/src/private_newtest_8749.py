from wrong_1_509 import *

import pytest
@pytest.mark.timeout(5)
def test_8749():
    assert search(12,[9]) == 1
