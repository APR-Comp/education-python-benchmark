from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_5824():
    assert search(8,[1, 5, 7, 51]) == 3
