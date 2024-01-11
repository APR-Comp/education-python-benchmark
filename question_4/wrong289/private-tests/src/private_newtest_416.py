from wrong_4_289 import *

import pytest
@pytest.mark.timeout(5)
def test_416():
    assert sort_age([('F', 19), ('F', 9), ('M', 4)]) == [('F', 19), ('F', 9), ('M', 4)]
