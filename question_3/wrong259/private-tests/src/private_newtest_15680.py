from wrong_3_259 import *

import pytest
@pytest.mark.timeout(5)
def test_15680():
    assert remove_extras([5]) == [5]
