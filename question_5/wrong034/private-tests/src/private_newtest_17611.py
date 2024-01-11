from wrong_5_034 import *

import pytest
@pytest.mark.timeout(5)
def test_17611():
    assert top_k([19, 18],1) == [19]
