from wrong_3_234 import *

import pytest
@pytest.mark.timeout(5)
def test_1061():
    assert remove_extras([30]) == [30]
