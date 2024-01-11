from wrong_5_029 import *

import pytest
@pytest.mark.timeout(5)
def test_4073():
    assert top_k([721, 80, 3],2) == [721, 80]
