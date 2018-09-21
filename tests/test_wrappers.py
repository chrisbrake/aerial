import signal as s
from aerial import Feed, wrappers as w


def test_feed_init():
    """ Confirm feed is initialized if it is None """
    w.feed = None
    w.received(s.SIGINT)
    assert isinstance(w.feed, Feed)


def test_received_false():
    """ Confirm the method returns False if no signal recieved """
    assert not w.received(s.SIGINT)


def test_received_true():
    """ Confirm we get back True if signal retrieved """
    w.feed = None  # reset
    w.received(s.SIGINT)  # init
    w.feed._receiver(s.SIGINT, 'frame')
    assert w.received(s.SIGINT)


def test_received_true_auto_awk_default():
    """ Confirm we get back True if signal retrieved, and then False again """
    w.feed = None  # reset
    w.received(s.SIGINT)  # init
    w.feed._receiver(s.SIGINT, 'frame')
    assert w.received(s.SIGINT)
    assert not w.received(s.SIGINT)


def test_received_true_auto_awk_true():
    """ Confirm we get back True if signal retrieved, and then False again """
    w.feed = None  # reset
    w.received(s.SIGINT)  # init
    w.feed._receiver(s.SIGINT, 'frame')
    assert w.received(s.SIGINT, awk=True)
    assert not w.received(s.SIGINT)


def test_received_true_auto_awk_false():
    """ Confirm we get back True if signal retrieved, and then True again """
    w.feed = None  # reset
    w.received(s.SIGINT)  # init
    w.feed._receiver(s.SIGINT, 'frame')
    assert w.received(s.SIGINT, awk=False)
    assert w.received(s.SIGINT, awk=True)
    assert not w.received(s.SIGINT)
