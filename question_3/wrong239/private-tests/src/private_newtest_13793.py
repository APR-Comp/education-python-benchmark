from wrong_3_239 import *

import pytest
@pytest.mark.timeout(5)
def test_13793():
    assert remove_extras([460, 608]) == [460, 608]
