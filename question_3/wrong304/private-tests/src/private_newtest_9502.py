from wrong_3_304 import *

import pytest
@pytest.mark.timeout(5)
def test_9502():
    assert remove_extras([14]) == [14]
