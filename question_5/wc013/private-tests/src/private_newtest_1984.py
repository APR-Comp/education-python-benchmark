from wrong_correct_5_013 import *

import pytest
@pytest.mark.timeout(5)
def test_1984():
    assert top_k([7, 49],0) == []
