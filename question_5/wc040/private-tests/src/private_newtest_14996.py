from wrong_correct_5_040 import *

import pytest
@pytest.mark.timeout(5)
def test_14996():
    assert top_k([6, 917886, 4, 206],2) == [917886, 206]
