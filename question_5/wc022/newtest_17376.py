from wrong_correct_5_022 import *

import pytest
@pytest.mark.timeout(5)
def test_17376():
    assert top_k([3],0) == []
