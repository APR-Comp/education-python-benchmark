from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_5120():
    assert remove_extras([6, 4185, 3]) == [6, 4185, 3]
