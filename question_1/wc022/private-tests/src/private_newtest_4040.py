from wrong_correct_1_022 import *

import pytest
@pytest.mark.timeout(5)
def test_4040():
    assert search(7,[5, 48, 49, 897, 978, 7589]) == 1
