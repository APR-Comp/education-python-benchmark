from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_17099():
    assert remove_extras([821, 1]) == [821, 1]
