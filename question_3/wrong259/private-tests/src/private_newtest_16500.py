from wrong_3_259 import *

import pytest
@pytest.mark.timeout(5)
def test_16500():
    assert remove_extras([61056]) == [61056]
