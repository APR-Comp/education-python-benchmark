from wrong_correct_5_004 import *

import pytest
@pytest.mark.timeout(5)
def test_14773():
    assert top_k([9],0) == []
