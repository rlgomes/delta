"""
deltas parse unittests
"""

import unittest

from datetime import datetime, timedelta

from robber import expect

from delta import parse

class ParseTest(unittest.TestCase):

    def test_1_milliseconds_parsing(self):
        delta = timedelta(milliseconds=1)
        expect(parse('1 milliseconds')).to.eq(delta)
        expect(parse('1 millisecond')).to.eq(delta)
        expect(parse('1 millis')).to.eq(delta)
        expect(parse('1 ms')).to.eq(delta)
        expect(parse('1ms')).to.eq(delta)

    def test_5_milliseconds_parsing(self):
        delta = timedelta(milliseconds=5)
        expect(parse('5 milliseconds')).to.eq(delta)
        expect(parse('5 millisecond')).to.eq(delta)
        expect(parse('5 millis')).to.eq(delta)
        expect(parse('5 ms')).to.eq(delta)
        expect(parse('5ms')).to.eq(delta)

    def test_fractional_milliseconds_parsing(self):
        delta = timedelta(milliseconds=5, microseconds=300)
        expect(parse('5.3 milliseconds')).to.eq(delta)
        expect(parse('5.3 millisecond')).to.eq(delta)
        expect(parse('5.3 millis')).to.eq(delta)
        expect(parse('5.3 ms')).to.eq(delta)
        expect(parse('5.3ms')).to.eq(delta)

    def test_1_seconds_parsing(self):
        delta = timedelta(seconds=1)
        expect(parse('1 seconds')).to.eq(delta)
        expect(parse('1 second')).to.eq(delta)
        expect(parse('1 s')).to.eq(delta)
        expect(parse('1s')).to.eq(delta)

    def test_5_seconds_parsing(self):
        delta = timedelta(seconds=5)
        expect(parse('5 seconds')).to.eq(delta)
        expect(parse('5 second')).to.eq(delta)
        expect(parse('5 s')).to.eq(delta)
        expect(parse('5s')).to.eq(delta)

    def test_fractional_seconds_parsing(self):
        delta = timedelta(seconds=5, milliseconds=300)
        expect(parse('5.3 seconds')).to.eq(delta)
        expect(parse('5.3 second')).to.eq(delta)
        expect(parse('5.3 s')).to.eq(delta)
        expect(parse('5.3s')).to.eq(delta)

    def test_1_minutes_parsing(self):
        delta = timedelta(minutes=1)
        expect(parse('1 minutes')).to.eq(delta)
        expect(parse('1 minute')).to.eq(delta)
        expect(parse('1 mins')).to.eq(delta)
        expect(parse('1 min')).to.eq(delta)
        expect(parse('1min')).to.eq(delta)
        expect(parse('1m')).to.eq(delta)

    def test_5_minutes_parsing(self):
        delta = timedelta(minutes=5)
        expect(parse('5 minutes')).to.eq(delta)
        expect(parse('5 minute')).to.eq(delta)
        expect(parse('5 mins')).to.eq(delta)
        expect(parse('5 min')).to.eq(delta)
        expect(parse('5min')).to.eq(delta)
        expect(parse('5m')).to.eq(delta)

    def test_fractional_minutes_parsing(self):
        seconds = 60 * 0.3
        delta = timedelta(minutes=5, seconds=seconds)
        expect(parse('5.3 minutes')).to.eq(delta)
        expect(parse('5.3 minute')).to.eq(delta)
        expect(parse('5.3 mins')).to.eq(delta)
        expect(parse('5.3 min')).to.eq(delta)
        expect(parse('5.3min')).to.eq(delta)
        expect(parse('5.3m')).to.eq(delta)

    def test_1_hours_parsing(self):
        delta = timedelta(hours=1)
        expect(parse('1 hours')).to.eq(delta)
        expect(parse('1 hour')).to.eq(delta)
        expect(parse('1 h')).to.eq(delta)
        expect(parse('1h')).to.eq(delta)

    def test_5_hours_parsing(self):
        delta = timedelta(hours=5)
        expect(parse('5 hours')).to.eq(delta)
        expect(parse('5 hour')).to.eq(delta)
        expect(parse('5 h')).to.eq(delta)
        expect(parse('5h')).to.eq(delta)

    def test_fractional_hours_parsing(self):
        minutes = 60 * 0.3
        delta = timedelta(hours=5, minutes=minutes)
        expect(parse('5.3 hours')).to.eq(delta)
        expect(parse('5.3 hour')).to.eq(delta)
        expect(parse('5.3 h')).to.eq(delta)
        expect(parse('5.3h')).to.eq(delta)

    def test_1_days_parsing(self):
        delta = timedelta(days=1)
        expect(parse('1 days')).to.eq(delta)
        expect(parse('1 day')).to.eq(delta)
        expect(parse('1 d')).to.eq(delta)
        expect(parse('1d')).to.eq(delta)

    def test_5_days_parsing(self):
        delta = timedelta(days=5)
        expect(parse('5 days')).to.eq(delta)
        expect(parse('5 day')).to.eq(delta)
        expect(parse('5 d')).to.eq(delta)
        expect(parse('5d')).to.eq(delta)

    def test_fractional_days_parsing(self):
        hours = 24 * 0.3
        delta = timedelta(days=5, hours=hours)
        expect(parse('5.3 days')).to.eq(delta)
        expect(parse('5.3 day')).to.eq(delta)
        expect(parse('5.3 d')).to.eq(delta)
        expect(parse('5.3d')).to.eq(delta)

    def test_1_weeks_parsing(self):
        delta = timedelta(weeks=1)
        expect(parse('1 weeks')).to.eq(delta)
        expect(parse('1 week')).to.eq(delta)
        expect(parse('1 w')).to.eq(delta)
        expect(parse('1w')).to.eq(delta)

    def test_5_weeks_parsing(self):
        delta = timedelta(weeks=5)
        expect(parse('5 weeks')).to.eq(delta)
        expect(parse('5 week')).to.eq(delta)
        expect(parse('5 w')).to.eq(delta)
        expect(parse('5w')).to.eq(delta)

    def test_fractional_weeks_parsing(self):
        days = 7 * 0.2
        delta = timedelta(weeks=5, days=days)
        expect(parse('5.2 weeks')).to.eq(delta)
        expect(parse('5.2 week')).to.eq(delta)
        expect(parse('5.2 w')).to.eq(delta)
        expect(parse('5.2w')).to.eq(delta)

    def test_1_months_parsing(self):
        date = datetime(2016, 1, 1)
        delta = timedelta(days=31)
        expect(parse('1 months', context=date)).to.eq(delta)
        expect(parse('1 month', context=date)).to.eq(delta)
        expect(parse('1M', context=date)).to.eq(delta)

    def test_5_months_parsing(self):
        date = datetime(2016, 1, 1)
        delta = timedelta(days=152)
        expect(parse('5 months', context=date)).to.eq(delta)
        expect(parse('5 month', context=date)).to.eq(delta)
        expect(parse('5M', context=date)).to.eq(delta)

    def test_fractional_months_parsing(self):
        date = datetime(2016, 1, 1)
        days = 31 + 29 + 31 + 30 + 31 + 0.2 * 30
        delta = timedelta(days=days)
        expect(parse('5.2 months', context=date)).to.eq(delta)
        expect(parse('5.2 month', context=date)).to.eq(delta)
        expect(parse('5.2M', context=date)).to.eq(delta)

    def test_1_years_parsing(self):
        date = datetime(2017, 1, 1)
        delta = timedelta(days=365)
        expect(parse('1 years', context=date)).to.eq(delta)
        expect(parse('1 year', context=date)).to.eq(delta)
        expect(parse('1 y', context=date)).to.eq(delta)
        expect(parse('1y', context=date)).to.eq(delta)

    def test_5_years_parsing(self):
        date = datetime(2017, 1, 1)
        delta = timedelta(days=365 * 5 + 1)
        expect(parse('5 years', context=date)).to.eq(delta)
        expect(parse('5 year', context=date)).to.eq(delta)
        expect(parse('5 y', context=date)).to.eq(delta)
        expect(parse('5y', context=date)).to.eq(delta)

    def test_fractional_years_parsing(self):
        date = datetime(2017, 1, 1)
        days = 365 * 2.0 + 365 / 2.0
        delta = timedelta(days=days)
        expect(parse('2.5 years', context=date)).to.eq(delta)
        expect(parse('2.5 year', context=date)).to.eq(delta)
        expect(parse('2.5 y', context=date)).to.eq(delta)
        expect(parse('2.5y', context=date)).to.eq(delta)

    def test_seconds_and_milliseconds(self):
        delta = timedelta(seconds=2, milliseconds=1)
        expect(parse('2 seconds and 1 milliseconds')).to.eq(delta)
        expect(parse('2 seconds and 1 millisecond')).to.eq(delta)
        expect(parse('2 seconds, 1 millisecond')).to.eq(delta)
        expect(parse('2 seconds 1 ms')).to.eq(delta)
        expect(parse('2 s 1 ms')).to.eq(delta)
        expect(parse('2 s, 1 ms')).to.eq(delta)
        expect(parse('2s, 1ms')).to.eq(delta)

    def test_minutes_and_seconds(self):
        delta = timedelta(minutes=2, seconds=1)
        expect(parse('2 minutes and 1 seconds')).to.eq(delta)
        expect(parse('2 minutes and 1 second')).to.eq(delta)
        expect(parse('2 minutes, 1 second')).to.eq(delta)
        expect(parse('2 minutes 1 s')).to.eq(delta)
        expect(parse('2 mins 1 s')).to.eq(delta)
        expect(parse('2 min, 1 s')).to.eq(delta)
        expect(parse('2min, 1s')).to.eq(delta)

    def test_hours_and_minutes(self):
        delta = timedelta(hours=2, minutes=1)
        expect(parse('2 hours and 1 minutes')).to.eq(delta)
        expect(parse('2 hours and 1 minute')).to.eq(delta)
        expect(parse('2 hours, 1 minute')).to.eq(delta)
        expect(parse('2 hours 1 min')).to.eq(delta)
        expect(parse('2 hour 1 mins')).to.eq(delta)
        expect(parse('2 h, 1 min')).to.eq(delta)
        expect(parse('2h, 1min')).to.eq(delta)

    def test_days_and_hours(self):
        delta = timedelta(days=2, hours=1)
        expect(parse('2 days and 1 hours')).to.eq(delta)
        expect(parse('2 days and 1 hour')).to.eq(delta)
        expect(parse('2 days, 1 hour')).to.eq(delta)
        expect(parse('2 days 1 hour')).to.eq(delta)
        expect(parse('2 days 1 h')).to.eq(delta)
        expect(parse('2 d, 1 h')).to.eq(delta)
        expect(parse('2d, 1h')).to.eq(delta)

    def test_weeks_and_days(self):
        delta = timedelta(weeks=2, days=1)
        expect(parse('2 weeks and 1 days')).to.eq(delta)
        expect(parse('2 weeks and 1 day')).to.eq(delta)
        expect(parse('2 weeks, 1 day')).to.eq(delta)
        expect(parse('2 weeks 1 day')).to.eq(delta)
        expect(parse('2 weeks 1 d')).to.eq(delta)
        expect(parse('2 w, 1 d')).to.eq(delta)
        expect(parse('2w, 1d')).to.eq(delta)

    def test_months_and_weeks(self):
        date = datetime(2016, 1, 1)
        # January 31 days + February 29 days (2016) + 7 days in a week
        days = 31 + 29 + 7
        delta = timedelta(days=days)
        expect(parse('2 months and 1 weeks', context=date)).to.eq(delta)
        expect(parse('2 months and 1 week', context=date)).to.eq(delta)
        expect(parse('2 months, 1 week', context=date)).to.eq(delta)
        expect(parse('2 month 1 week', context=date)).to.eq(delta)
        expect(parse('2 months 1 w', context=date)).to.eq(delta)
        expect(parse('2 month, 1 w', context=date)).to.eq(delta)
        expect(parse('2 M, 1 w', context=date)).to.eq(delta)
        expect(parse('2M, 1w', context=date)).to.eq(delta)

    def test_years_and_months(self):
        date = datetime(2017, 1, 1)
        # 365 days in 2017 and 2018 + 31 days in January
        days = 365 * 2 + 31
        delta = timedelta(days=days)
        expect(parse('2 years and 1 months', context=date)).to.eq(delta)
        expect(parse('2 years and 1 month', context=date)).to.eq(delta)
        expect(parse('2 years, 1 month', context=date)).to.eq(delta)
        expect(parse('2 years 1 month', context=date)).to.eq(delta)
        expect(parse('2 year 1 month', context=date)).to.eq(delta)
        expect(parse('2 year, 1 month', context=date)).to.eq(delta)
        expect(parse('2 y 1 M', context=date)).to.eq(delta)
        expect(parse('2y, 1M', context=date)).to.eq(delta)

    def test_years_months_and_weeks(self):
        date = datetime(2016, 1, 1)
        # 366 days 2016 + 31 days in January + 2 weeks * 7 days
        days = 366 + 31 + 7 * 2
        delta = timedelta(days=days)
        expect(parse('1 years and 1 month and 2 weeks', context=date)).to.eq(delta)
        expect(parse('1 years, 1 month and 2 weeks', context=date)).to.eq(delta)
        expect(parse('1 year 1 month 2 weeks', context=date)).to.eq(delta)
        expect(parse('1 y 1 M 2 w', context=date)).to.eq(delta)
        expect(parse('1y 1M 2w', context=date)).to.eq(delta)

    def test_years_and_weeks(self):
        date = datetime(2016, 1, 1)
        # 366 days 2016 + 2 weeks * 7 days
        days = 366 + 7 * 2
        delta = timedelta(days=days)
        expect(parse('1 years and 2 weeks', context=date)).to.eq(delta)
        expect(parse('1 year and 2 weeks', context=date)).to.eq(delta)
        expect(parse('1 year, 2 weeks', context=date)).to.eq(delta)
        expect(parse('1y, 2w', context=date)).to.eq(delta)

    def test_years_weeks_and_days(self):
        date = datetime(2016, 1, 1)
        # 366 days 2016 + 2 weeks * 7 days + 3 days
        days = 366 + 7 * 2 + 3
        delta = timedelta(days=days)
        expect(parse('1 year, 2 weeks and 3 days', context=date)).to.eq(delta)
        expect(parse('1 year, 2 weeks, 3 days', context=date)).to.eq(delta)
        expect(parse('1 y, 2 w, 3 d', context=date)).to.eq(delta)
        expect(parse('1y, 2w, 3d', context=date)).to.eq(delta)

    def test_with_everything(self):
        date = datetime(2016, 1, 1)
        # 366 + 365 + 31 (Jan 2018) + 29 (Feb 2018) + 2 weeks * 7 days + 3 days
        days = 366 + 365 + 31 + 29 + 7 * 2 + 3
        delta = timedelta(days=days, hours=24, minutes=25, seconds=60)
        expect(parse('2 years, 2 months, 2 weeks, 3 days, 24 hours, 25 minutes and 60 seconds', context=date)).to.eq(delta)
        expect(parse('2 year 2 months 2 weeks 3 days 24 hours 25 minutes 60 seconds', context=date)).to.eq(delta)
        expect(parse('2y 2M 2w 3d 24h 25min 60s', context=date)).to.eq(delta)

    def test_last_day_of_month_while_month_parsing(self):
        date = datetime(2016, 1, 31)
        expect(parse('1 month', context=date)).to.eq(timedelta(days=31))

    def test_last_day_of_month_while_year_parsing(self):
        date = datetime(2017, 1, 31)
        expect(parse('1 year', context=date)).to.eq(timedelta(days=365))

    def test_end_of_year_overflow(self):
        expect(parse('1 month', context=datetime(2016, 12, 31))).to.eq(timedelta(days=31))
    
    def test_days_in_year(self):
        expect(parse('1 year', context=datetime(2001, 1, 1))).to.eq(timedelta(days=365))
    
    def test_days_in_leap_year(self):
        expect(parse('1 year', context=datetime(2000, 1, 1))).to.eq(timedelta(days=366))

    def test_multi_year_overflow(self):
        # days in 2016 + days in 2017 + Jan of 2018 + Feb of 2018 + Mar of 2018
        delta = timedelta(days=365 + 365 + 31 + 29 + 31)
        expect(parse('27 months', context=datetime(2016, 1, 1))).to.eq(delta)
