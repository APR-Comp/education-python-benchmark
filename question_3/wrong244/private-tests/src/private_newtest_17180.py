from wrong_3_244 import *

import pytest
@pytest.mark.timeout(5)
def test_17180():
    assert remove_extras([20466, 2]) == [20466, 2]
