from wrong_3_224 import *

import pytest
@pytest.mark.timeout(5)
def test_7203():
    assert remove_extras([527]) == [527]
