from wrong_correct_5_049 import *

import pytest
@pytest.mark.timeout(5)
def test_15587():
    assert top_k([69, 6],1) == [69]
