from wrong_4_349 import *

import pytest
@pytest.mark.timeout(5)
def test_5388():
    assert sort_age([('F', 27), ('F', 29), ('F', 1), ('F', 14)]) == [('F', 29), ('F', 27), ('F', 14), ('F', 1)]
