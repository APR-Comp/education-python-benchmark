from wrong_correct_3_031 import *

import pytest
@pytest.mark.timeout(5)
def test_9608():
    assert remove_extras([41, 634, 260479]) == [41, 634, 260479]
