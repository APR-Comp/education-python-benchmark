from wrong_5_099 import *

import pytest
@pytest.mark.timeout(5)
def test_12032():
    assert top_k([50, 71],1) == [71]
