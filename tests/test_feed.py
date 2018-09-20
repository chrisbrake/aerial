import signal
from aerial import Feed


def test_init_false():
    """ Confirm the class starts falsey """
    assert not Feed()


def test_signal_addition_init_false():
    """ Confirm attempting to read a signal starts the recording """
    f = Feed()
    assert signal.SIGINT not in f.signals
    assert not f[signal.SIGINT]
    assert signal.SIGINT in f.signals


def test_signal_receive_converts_true():
    """ Confirm receipt of any signal converts feed object to truthy """
    f = Feed()
    assert not f[signal.SIGINT]
    f._receiver(signal.SIGINT, 'frame')
    assert f


def test_signal_awk_converts_false():
    """ Confirm awk the signal converts feed object to falsey """
    f = Feed()
    assert not f[signal.SIGINT]
    f._receiver(signal.SIGINT, 'frame')
    f[signal.SIGINT].awk()
    assert not f
