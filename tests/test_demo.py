import mock
from aerial import demo

demo.print = mock.Mock()
demo.time.sleep = mock.Mock()


def test_spinner():
    demo.trick()
    assert 30 == demo.print.call_count == demo.time.sleep.call_count