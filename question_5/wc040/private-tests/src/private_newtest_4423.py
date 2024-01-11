from wrong_correct_5_040 import *

import pytest
@pytest.mark.timeout(5)
def test_4423():
    assert top_k([4895, 8, 895],0) == []
