from wrong_correct_3_040 import *

import pytest
@pytest.mark.timeout(5)
def test_3872():
    assert remove_extras([60]) == [60]
