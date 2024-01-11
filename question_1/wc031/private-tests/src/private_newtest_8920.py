from wrong_correct_1_031 import *

import pytest
@pytest.mark.timeout(5)
def test_8920():
    assert search(36,[5, 9]) == 2
