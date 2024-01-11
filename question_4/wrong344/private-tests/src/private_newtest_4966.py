from wrong_4_344 import *

import pytest
@pytest.mark.timeout(5)
def test_4966():
    assert sort_age([('M', 5), ('F', 33)]) == [('F', 33), ('M', 5)]
