from wrong_correct_5_058 import *

import pytest
@pytest.mark.timeout(5)
def test_14173():
    assert top_k([7760, 9, 931],2) == [7760, 931]
