from wrong_correct_5_040 import *

import pytest
@pytest.mark.timeout(5)
def test_6476():
    assert top_k([57],0) == []