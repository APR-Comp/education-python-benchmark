from wrong_1_509 import *

import pytest
@pytest.mark.timeout(5)
def test_8145():
    assert search(9,[6, 55]) == 1
