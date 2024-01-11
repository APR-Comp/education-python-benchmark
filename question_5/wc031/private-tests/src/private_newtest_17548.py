from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17548():
    assert top_k([172],0) == []
