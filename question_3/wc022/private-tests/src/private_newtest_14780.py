from wrong_correct_3_022 import *

import pytest
@pytest.mark.timeout(5)
def test_14780():
    assert remove_extras([683, 19, 174]) == [683, 19, 174]
