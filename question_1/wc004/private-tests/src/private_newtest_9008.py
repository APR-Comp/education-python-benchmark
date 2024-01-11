from wrong_correct_1_004 import *

import pytest
@pytest.mark.timeout(5)
def test_9008():
    assert search(8749,[7, 99]) == 2
