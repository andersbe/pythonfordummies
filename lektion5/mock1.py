import time
from expensive_api_call import compute


def test_compute(mocker):
    mocker.patch("expensive_api_call.expensive_api_call", return_value=123)
    expected=124
    actual=compute(1)
    assert expected == actual
    
