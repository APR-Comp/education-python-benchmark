from wrong_correct_5_022 import *

import pytest
@pytest.mark.timeout(5)
def test_1148():
    assert top_k([6, 1, 5],0) == []
