from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_731():
    assert search(7,[3, 5, 70, 736893]) == 2
