from wrong_1_509 import *

import pytest
@pytest.mark.timeout(5)
def test_1090():
    assert search(2,[1, 4, 6, 110, 5398]) == 1
