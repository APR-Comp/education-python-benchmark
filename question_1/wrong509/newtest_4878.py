from wrong_1_509 import *

import pytest
@pytest.mark.timeout(5)
def test_4878():
    assert search(78,[1, 6, 160]) == 2
