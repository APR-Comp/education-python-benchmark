from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_15733():
    assert top_k([375, 197094],1) == [197094]
