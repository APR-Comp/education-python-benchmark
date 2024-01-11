from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_3215():
    assert remove_extras([1, 483, 99]) == [1, 483, 99]
