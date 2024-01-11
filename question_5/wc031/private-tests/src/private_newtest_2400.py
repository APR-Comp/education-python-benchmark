from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_2400():
    assert top_k([25, 78],1) == [78]
