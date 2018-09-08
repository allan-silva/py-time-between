from datetime import datetime, time, timedelta


ARBITRARY_DATE = datetime(1988, 3, 14)


def is_time_between(t, start, end):
    if start == end:
        return True
    day_add = 1 if end < start else 0
    end_add = 1 if day_add and end == time(0,0,0,0) else 0
    td_time_start = timedelta(hours=start.hour,
                              minutes=start.minute,
                              seconds=start.second,
                              microseconds=start.microsecond)
    td_time_end = timedelta(days=day_add + end_add,
                            hours=end.hour,
                            minutes=end.minute,
                            seconds=end.second,
                            microseconds=end.microsecond)
    td_testing = timedelta(days=day_add,
                           hours=t.hour,
                           minutes=t.minute,
                           seconds=t.second,
                           microseconds=t.microsecond)
    start_date = ARBITRARY_DATE + td_time_start
    end_date = ARBITRARY_DATE + td_time_end
    testing_date = ARBITRARY_DATE + td_testing
    return start_date <= testing_date and testing_date <= end_date
