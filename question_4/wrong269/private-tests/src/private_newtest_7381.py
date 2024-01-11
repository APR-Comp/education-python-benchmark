from wrong_4_269 import *

import pytest
@pytest.mark.timeout(5)
def test_7381():
    assert sort_age([('M', 5), ('M', 28), ('F', 7), ('M', 38)]) == [('M', 38), ('M', 28), ('F', 7), ('M', 5)]
