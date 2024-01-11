from wrong_5_099 import *

import pytest
@pytest.mark.timeout(5)
def test_18656():
    assert top_k([39],0) == []
