from wrong_5_034 import *

import pytest
@pytest.mark.timeout(5)
def test_3464():
    assert top_k([66255, 777, 59, 9],3) == [66255, 777, 59]
