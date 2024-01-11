from wrong_3_239 import *

import pytest
@pytest.mark.timeout(5)
def test_4708():
    assert remove_extras([5]) == [5]
