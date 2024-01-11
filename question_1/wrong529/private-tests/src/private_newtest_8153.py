from wrong_1_529 import *

import pytest
@pytest.mark.timeout(5)
def test_8153():
    assert search(60691,[6, 49, 364, 366, 6210]) == 5
