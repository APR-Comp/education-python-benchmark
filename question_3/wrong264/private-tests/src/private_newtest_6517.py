from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_6517():
    assert remove_extras([52, 6]) == [52, 6]
