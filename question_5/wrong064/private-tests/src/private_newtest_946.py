from wrong_5_064 import *

import pytest
@pytest.mark.timeout(5)
def test_946():
    assert top_k([7, 128],1) == [128]
