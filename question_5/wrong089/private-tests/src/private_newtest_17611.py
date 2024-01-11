from wrong_5_089 import *

import pytest
@pytest.mark.timeout(5)
def test_17611():
    assert top_k([19, 18],1) == [19]
