from wrong_5_044 import *

import pytest
@pytest.mark.timeout(5)
def test_10694():
    assert top_k([60, 991, 93, 29, 5],4) == [991, 93, 60, 29]
