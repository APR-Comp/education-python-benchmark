from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_1061():
    assert remove_extras([30]) == [30]
