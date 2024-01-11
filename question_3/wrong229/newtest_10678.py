from wrong_3_229 import *

import pytest
@pytest.mark.timeout(5)
def test_10678():
    assert remove_extras([27]) == [27]
