from aerial import signalData


def test_init_false():
    """ Confirm the class starts falsey """
    assert not signalData.SignalData(1)


def test_init_rec_true():
    """ Confirm recording a signal converts it truthy """
    assert signalData.SignalData(1).rec('frame')


def test_init_awk_false():
    """ Confirm recording a signal and then acknowledging converts it falsey """
    assert not signalData.SignalData(1).rec('frame').awk()
