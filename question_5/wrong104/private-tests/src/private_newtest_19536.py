from wrong_5_104 import *

import pytest
@pytest.mark.timeout(5)
def test_19536():
    assert top_k([86, 2],1) == [86]
