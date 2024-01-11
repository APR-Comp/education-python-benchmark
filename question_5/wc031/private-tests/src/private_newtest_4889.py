from wrong_correct_5_031 import *

import pytest
@pytest.mark.timeout(5)
def test_4889():
    assert top_k([1959, 7],1) == [1959]
