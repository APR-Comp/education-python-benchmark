from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17611():
    assert top_k([19, 18],1) == [19]
