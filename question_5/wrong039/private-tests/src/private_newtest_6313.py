from wrong_5_039 import *

import pytest
@pytest.mark.timeout(5)
def test_6313():
    assert top_k([988, 9, 5],1) == [988]
