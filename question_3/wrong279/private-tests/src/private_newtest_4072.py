from wrong_3_279 import *

import pytest
@pytest.mark.timeout(5)
def test_4072():
    assert remove_extras([77, 1, 8]) == [77, 1, 8]
