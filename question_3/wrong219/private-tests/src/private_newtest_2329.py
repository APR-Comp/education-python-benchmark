from wrong_3_219 import *

import pytest
@pytest.mark.timeout(5)
def test_2329():
    assert remove_extras([2, 6, 3, 62]) == [2, 6, 3, 62]
