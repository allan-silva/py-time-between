from datetime import time
from timebetween import is_time_between


def test_is_time_between():
    t, s, e = time(0), time(0), time(0)
    assert is_time_between(t, s, e)

    t, s, e = time(0, 0, 0, 1), time(0), time(0, 0, 0, 2)
    assert is_time_between(t, s, e)

    t, s, e = time(0, 0, 0, 1), time(0, 0, 0, 1), time(0, 0, 0, 2)
    assert is_time_between(t, s, e)

    t, s, e = time(0, 0, 0, 2), time(0, 0, 0, 1), time(0, 0, 0, 2)
    assert is_time_between(t, s, e)

    t, s, e = time(0, 0, 1), time(23, 59, 59), time(0, 0, 2)
    assert is_time_between(t, s, e)

    t, s, e = time(12, 0, 0), time(23, 59, 59), time(0, 0, 0)
    assert is_time_between(t, s, e)

    t, s, e = time(23, 59, 57), time(23, 59, 59), time(23, 59, 57)
    assert is_time_between(t, s, e)

    t, s, e = time(23, 59, 58), time(23, 59, 59), time(23, 59, 57)
    assert not is_time_between(t, s, e)

    t, s, e = time(22), time(22), time(5, 59, 59)
    assert is_time_between(t, s, e)

    # Hey, did you see a uncovered test case?
    # Please, open a PR.
