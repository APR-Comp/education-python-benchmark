from wrong_5_039 import *

import pytest
@pytest.mark.timeout(5)
def test_16614():
    assert top_k([4552, 64, 99, 5, 8],3) == [4552, 99, 64]
