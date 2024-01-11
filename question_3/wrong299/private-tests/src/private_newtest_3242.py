from wrong_3_299 import *

import pytest
@pytest.mark.timeout(5)
def test_3242():
    assert remove_extras([722]) == [722]
