from wrong_3_219 import *

import pytest
@pytest.mark.timeout(5)
def test_111():
    assert remove_extras([4083, 3190]) == [4083, 3190]
