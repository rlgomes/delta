"""
deltas parse unittests
"""

import unittest

from datetime import datetime, timedelta

from robber import expect

from delta import parse

class ParseTest(unittest.TestCase):

    def test_1_seconds_parsing(self):
        expect(parse('1 seconds')).to.eq(timedelta(seconds=1))
        expect(parse('1 second')).to.eq(timedelta(seconds=1))
        expect(parse('1 s')).to.eq(timedelta(seconds=1))
        expect(parse('1s')).to.eq(timedelta(seconds=1))

    def test_n_seconds_parsing(self):
        expect(parse('5 seconds')).to.eq(timedelta(seconds=5))
        expect(parse('5 second')).to.eq(timedelta(seconds=5))
        expect(parse('5 s')).to.eq(timedelta(seconds=5))
        expect(parse('5s')).to.eq(timedelta(seconds=5))

    def test_1_minutes_parsing(self):
        expect(parse('1 minutes')).to.eq(timedelta(minutes=1))
        expect(parse('1 minute')).to.eq(timedelta(minutes=1))
        expect(parse('1 mins')).to.eq(timedelta(minutes=1))
        expect(parse('1 min')).to.eq(timedelta(minutes=1))
        expect(parse('1min')).to.eq(timedelta(minutes=1))

    def test_5_minutes_parsing(self):
        expect(parse('5 minutes')).to.eq(timedelta(minutes=5))
        expect(parse('5 minute')).to.eq(timedelta(minutes=5))
        expect(parse('5 mins')).to.eq(timedelta(minutes=5))
        expect(parse('5 min')).to.eq(timedelta(minutes=5))
        expect(parse('5min')).to.eq(timedelta(minutes=5))

    def test_1_hours_parsing(self):
        expect(parse('1 hours')).to.eq(timedelta(hours=1))
        expect(parse('1 hour')).to.eq(timedelta(hours=1))
        expect(parse('1 h')).to.eq(timedelta(hours=1))
        expect(parse('1h')).to.eq(timedelta(hours=1))

    def test_n_hours_parsing(self):
        expect(parse('5 hours')).to.eq(timedelta(hours=5))
        expect(parse('5 hour')).to.eq(timedelta(hours=5))
        expect(parse('5 h')).to.eq(timedelta(hours=5))
        expect(parse('5h')).to.eq(timedelta(hours=5))

    def test_1_days_parsing(self):
        expect(parse('1 days')).to.eq(timedelta(days=1))
        expect(parse('1 day')).to.eq(timedelta(days=1))
        expect(parse('1 d')).to.eq(timedelta(days=1))
        expect(parse('1d')).to.eq(timedelta(days=1))

    def test_n_days_parsing(self):
        expect(parse('5 days')).to.eq(timedelta(days=5))
        expect(parse('5 day')).to.eq(timedelta(days=5))
        expect(parse('5 d')).to.eq(timedelta(days=5))
        expect(parse('5d')).to.eq(timedelta(days=5))

    def test_1_weeks_parsing(self):
        expect(parse('1 weeks')).to.eq(timedelta(weeks=1))
        expect(parse('1 week')).to.eq(timedelta(weeks=1))
        expect(parse('1 w')).to.eq(timedelta(weeks=1))
        expect(parse('1w')).to.eq(timedelta(weeks=1))

    def test_n_weeks_parsing(self):
        expect(parse('5 weeks')).to.eq(timedelta(weeks=5))
        expect(parse('5 week')).to.eq(timedelta(weeks=5))
        expect(parse('5 w')).to.eq(timedelta(weeks=5))
        expect(parse('5w')).to.eq(timedelta(weeks=5))

    def test_1_months_parsing(self):
        date = datetime(2016, 1, 1)
        expect(parse('1 months', context=date)).to.eq(timedelta(days=31))
        expect(parse('1 month', context=date)).to.eq(timedelta(days=31))
        expect(parse('1m', context=date)).to.eq(timedelta(days=31))

    def test_n_months_parsing(self):
        date = datetime(2016, 1, 1)
        expect(parse('5 months', context=date)).to.eq(timedelta(days=152))
        expect(parse('5 month', context=date)).to.eq(timedelta(days=152))
        expect(parse('5m', context=date)).to.eq(timedelta(days=152))

    def test_1_years_parsing(self):
        date = datetime(2016, 1, 1)
        expect(parse('1 years', context=date)).to.eq(timedelta(days=365))
        expect(parse('1 year', context=date)).to.eq(timedelta(days=365))
        expect(parse('1 y', context=date)).to.eq(timedelta(days=365))
        expect(parse('1y', context=date)).to.eq(timedelta(days=365))

    def test_n_years_parsing(self):
        date = datetime(2016, 1, 1)
        expect(parse('5 years', context=date)).to.eq(timedelta(days=365*5+1))
        expect(parse('5 year', context=date)).to.eq(timedelta(days=365*5+1))
        expect(parse('5 y', context=date)).to.eq(timedelta(days=365*5+1))
        expect(parse('5y', context=date)).to.eq(timedelta(days=365*5+1))

    def test_minutes_and_seconds(self):
        expect(parse('2 minutes and 1 seconds')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2 minutes and 1 second')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2 minutes, 1 second')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2 minutes 1 s')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2 mins 1 s')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2 min, 1 s')).to.eq(timedelta(minutes=2, seconds=1))
        expect(parse('2min, 1s')).to.eq(timedelta(minutes=2, seconds=1))

    def test_hours_and_minutes(self):
        expect(parse('2 hours and 1 minutes')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2 hours and 1 minute')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2 hours, 1 minute')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2 hours 1 min')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2 hour 1 mins')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2 h, 1 min')).to.eq(timedelta(hours=2, minutes=1))
        expect(parse('2h, 1min')).to.eq(timedelta(hours=2, minutes=1))

    def test_days_and_hours(self):
        expect(parse('2 days and 1 hours')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2 days and 1 hour')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2 days, 1 hour')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2 days 1 hour')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2 days 1 h')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2 d, 1 h')).to.eq(timedelta(days=2, hours=1))
        expect(parse('2d, 1h')).to.eq(timedelta(days=2, hours=1))

    def test_weeks_and_days(self):
        expect(parse('2 weeks and 1 days')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2 weeks and 1 day')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2 weeks, 1 day')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2 weeks 1 day')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2 weeks 1 d')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2 w, 1 d')).to.eq(timedelta(weeks=2, days=1))
        expect(parse('2w, 1d')).to.eq(timedelta(weeks=2, days=1))

    def test_months_and_weeks(self):
        date = datetime(2016, 1, 1)
        # January 31 days + February 29 days (2016) + 7 days in a week
        days = 31 + 29 + 7
        expect(parse('2 months and 1 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 months and 1 week', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 months, 1 week', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 month 1 week', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 months 1 w', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 month, 1 w', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 m, 1 w', context=date)).to.eq(timedelta(days=days))
        expect(parse('2m, 1w', context=date)).to.eq(timedelta(days=days))

    def test_years_and_months(self):
        date = datetime(2016, 1, 1)
        # 365 days in 2016 and 2017 + 31 days in January
        days = 365 * 2 + 31
        expect(parse('2 years and 1 months', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 years and 1 month', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 years, 1 month', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 years 1 month', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 year 1 month', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 year, 1 month', context=date)).to.eq(timedelta(days=days))
        expect(parse('2 y 1 m', context=date)).to.eq(timedelta(days=days))
        expect(parse('2y, 1m', context=date)).to.eq(timedelta(days=days))

    def test_years_months_and_weeks(self):
        date = datetime(2016, 1, 1)
        # 365 days 2016 + 31 days in January + 2 weeks * 7 days
        days = 365 + 31 + 7 * 2
        expect(parse('1 years and 1 month and 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 years, 1 month and 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 year 1 month 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 y 1 m 2 w', context=date)).to.eq(timedelta(days=days))
        expect(parse('1y 1m 2w', context=date)).to.eq(timedelta(days=days))

    def test_years_and_weeks(self):
        date = datetime(2016, 1, 1)
        # 365 days 2016 + 2 weeks * 7 days
        days = 365 + 7 * 2
        expect(parse('1 years and 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 year and 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 year, 2 weeks', context=date)).to.eq(timedelta(days=days))
        expect(parse('1y, 2w', context=date)).to.eq(timedelta(days=days))

    def test_years_weeks_and_days(self):
        date = datetime(2016, 1, 1)
        # 365 days 2016 + 2 weeks * 7 days + 3 days
        days = 365 + 7 * 2 + 3
        expect(parse('1 year, 2 weeks and 3 days', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 year, 2 weeks, 3 days', context=date)).to.eq(timedelta(days=days))
        expect(parse('1 y, 2 w, 3 d', context=date)).to.eq(timedelta(days=days))
        expect(parse('1y, 2w, 3d', context=date)).to.eq(timedelta(days=days))

    def test_with_everything(self):
        date = datetime(2016, 1, 1)
        # 365 * 2 + 31 (Jan 2016) + 29 (Feb 2016) + 2 weeks * 7 days + 3 days
        days = 365 * 2 + 31 + 29 + 7 * 2 + 3
        tdelta = timedelta(days=days, hours=24, minutes=25, seconds=60)
        expect(parse('2 years, 2 months, 2 weeks, 3 days, 24 hours, 25 minutes and 60 seconds', context=date)).to.eq(tdelta)
        expect(parse('2 year 2 months 2 weeks 3 days 24 hours 25 minutes 60 seconds', context=date)).to.eq(tdelta)
        expect(parse('2y 2m 2w 3d 24h 25min 60s', context=date)).to.eq(tdelta)

