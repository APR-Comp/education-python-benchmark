from wrong_3_229 import *

import pytest
@pytest.mark.timeout(5)
def test_9608():
    assert remove_extras([41, 634, 260479]) == [41, 634, 260479]
