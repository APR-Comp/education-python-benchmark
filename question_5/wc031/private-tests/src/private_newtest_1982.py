from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_1982():
    assert top_k([7, 37, 7, 2],3) == [37, 7, 7]