from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_2217():
    assert remove_extras([59, 2, 94]) == [59, 2, 94]
