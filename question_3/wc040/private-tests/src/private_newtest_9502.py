from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_9502():
    assert remove_extras([14]) == [14]