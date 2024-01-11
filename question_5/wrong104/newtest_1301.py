from wrong_5_104 import *

import pytest
@pytest.mark.timeout(5)
def test_1301():
    assert top_k([59834959, 257, 2],2) == [59834959, 257]
