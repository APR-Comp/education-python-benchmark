from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_9452():
    assert remove_extras([44]) == [44]
