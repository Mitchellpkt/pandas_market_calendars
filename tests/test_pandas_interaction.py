# Test from pandas-market-calendars issue: #301 "importing this package alters the behavior of pandas"
# Opened by erikhansenwong with the below test proposed
# See https://github.com/rsheftel/pandas_market_calendars/issues/301

import pytest

def test_custom_business_day():
    import pandas as pd
    from pandas.tseries.holiday import MO, AbstractHolidayCalendar, Holiday
    from pandas.tseries.offsets import CustomBusinessDay

    USMemorialDay = Holiday(
        "Memorial Day", month=5, day=31, offset=pd.DateOffset(weekday=MO(-1))
    )

    class ExampleCalendar(AbstractHolidayCalendar):
        rules = [USMemorialDay]

    bday1 = CustomBusinessDay(calendar=ExampleCalendar())
    bday2 = CustomBusinessDay(calendar=ExampleCalendar())

    # this assertion passes
    assert bday1 == bday2

    # but then we import pandas_market_calendars and try the same thing ...
    import pandas_market_calendars

    bday3 = CustomBusinessDay(calendar=ExampleCalendar())

    # and now this assertion fails
    assert bday1 == bday3