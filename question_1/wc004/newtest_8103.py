from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_8103():
    assert search(27,[1, 3, 8, 97]) == 3
