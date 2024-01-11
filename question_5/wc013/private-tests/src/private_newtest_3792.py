from wrong_correct_5_013 import *

import pytest
@pytest.mark.timeout(5)
def test_3792():
    assert top_k([6],0) == []
