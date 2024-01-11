from wrong_5_074 import *

import pytest
@pytest.mark.timeout(5)
def test_2400():
    assert top_k([25, 78],1) == [78]
