from wrong_5_024 import *

import pytest
@pytest.mark.timeout(5)
def test_3792():
    assert top_k([6],0) == []
