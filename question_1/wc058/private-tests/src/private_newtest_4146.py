from wrong_correct_1_058 import *

import pytest
@pytest.mark.timeout(5)
def test_4146():
    assert search(94,[4, 5, 8, 57, 278, 5624092]) == 4
