"""
deltas parse module
"""
import calendar
import re

from datetime import datetime, timedelta


def _get_duration_re():
    """
    return the duration matching regular expression
    """
    duration_matchers = [
        ('years', 'y(ear)?s?'),
        ('months', 'm(?!i|s)(onth)?s?'),
        ('weeks', 'w(eek)?s?'),
        ('days', 'd(ay)?s?'),
        ('hours', 'h(our)?s?'),
        ('minutes', 'min(ute)?s?'),
        ('seconds', 's(econd)?s?'),
        ('milliseconds', '(ms|millis(econd)?s?)')
    ]
    expression = []

    for (key, matcher) in duration_matchers:
        expression.append(r'(?:(?P<%s>\d+(\.\d+)?)(?:[\t ]*(?:%s)))?' % (key, matcher))

    return re.compile(r'[\t ]*(?:\,)?(?:and)?[\t ]*'.join(expression))

def parse(duration, context=None):
    """
    parse the duration string which contains a human readable duration and
    return a datetime.timedelta object representing that duration

    arguments:
        duration - the duration string following a notation like so:
                   "1 hour"
                   "1 month and 3 days" "1 year 2 weeks and 75 days"
                   "1 year, 75 days and 33 seconds"
                   ...
                   etc

        context - the context keyword argument is used to provide the current
                  datetime context object used when calculating years and
                  months which are dependent on the "current time" you're
                  calculating the relative delta in relation to.
    """
    matcher = _get_duration_re().match(duration)

    if matcher is None or matcher.end() < len(duration):
        raise Exception('unsupported duration "%s"' % duration)

    else:
        result = timedelta()

        if context is None:
            context = datetime.now()

        year = context.year
        month = context.month
        day = context.day

        for (key, value) in matcher.groupdict().items():
            weeks = 0
            days = 0
            hours = 0
            minutes = 0
            seconds = 0
            milliseconds = 0
            microseconds = 0

            if value is not None:
                value = float(value)
                whole = int(value)
                fraction = abs(whole - value)

                if key == 'years':
                    start = datetime(year, month, day)
                    end = datetime(year + whole, month, day)

                    # add remaining days for fraction part of year
                    days_in_year = (datetime(year + whole, 12, 31) -
                                    datetime(year + whole, 1, 1)).days + 1
                    end += timedelta(days=(fraction * days_in_year) - 1)

                    seconds = (end - start).total_seconds()

                elif key == 'months':
                    # figure out how many whole years and left over months and
                    # then let pythons datetime do all the work
                    years = whole / 12
                    months = whole % 12
                    start = datetime(year, month, day)
                    end = datetime(year + years, month + months, day)

                    # add remaining days for fraction part of the month
                    end_year = year + years
                    end_month = month + months
                    _, end_day = calendar.monthrange(end_year, end_month + 1)
                    days_in_month = (datetime(end_year, end_month + 1, end_day) -
                                     datetime(end_year, end_month + 1, 1)).days

                    end += timedelta(days=(fraction * days_in_month))

                    seconds = (end - start).total_seconds()

                elif key == 'weeks':
                    weeks = whole
                    days = fraction * 7

                elif key == 'days':
                    days = whole
                    hours = fraction * 24

                elif key == 'hours':
                    hours = whole
                    minutes = fraction * 60

                elif key == 'minutes':
                    minutes = whole
                    seconds = fraction * 60

                elif key == 'seconds':
                    seconds = whole
                    milliseconds = fraction

                elif key == 'milliseconds':
                    milliseconds = whole
                    microseconds = fraction

                result += timedelta(weeks=weeks,
                                    days=days,
                                    hours=hours,
                                    minutes=minutes,
                                    seconds=seconds,
                                    milliseconds=milliseconds,
                                    microseconds=microseconds)

        return result
