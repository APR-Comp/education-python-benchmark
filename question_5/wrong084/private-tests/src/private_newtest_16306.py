from wrong_5_084 import *

import pytest
@pytest.mark.timeout(5)
def test_16306():
    assert top_k([97, 693],1) == [693]
