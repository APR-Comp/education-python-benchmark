from wrong_3_239 import *

import pytest
@pytest.mark.timeout(5)
def test_17563():
    assert remove_extras([1, 4178, 238, 80, 8, 7, 3]) == [1, 4178, 238, 80, 8, 7, 3]
