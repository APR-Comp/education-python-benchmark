from wrong_correct_5_058 import *

import pytest
@pytest.mark.timeout(5)
def test_301():
    assert top_k([25520, 18, 5],1) == [25520]
