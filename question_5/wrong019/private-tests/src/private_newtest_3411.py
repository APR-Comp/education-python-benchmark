from wrong_5_019 import *

import pytest
@pytest.mark.timeout(5)
def test_3411():
    assert top_k([4, 7982004, 5, 29, 9, 21, 286, 70, 3768],2) == [7982004, 3768]
