"""
deltas parse module
"""

import re

from datetime import datetime, timedelta


def _get_duration_re():
    """
    return the duration matching regular expression
    """
    duration_matchers = [
        ('years', 'y(ear)?s?'),
        ('months', 'm(?!i)(onth)?s?'),
        ('weeks', 'w(eek)?s?'),
        ('days', 'd(ay)?s?'),
        ('hours', 'h(our)?s?'),
        ('minutes', 'min(ute)?s?'),
        ('seconds', 's(econd)?s?')
    ]
    expression = []

    for (key, matcher) in duration_matchers:
        expression.append(r'(?:(?P<%s>\d+)(?:[\t ]*(?:%s)))?' % (key, matcher))

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
            if value is not None:
                value = int(value)
                if key == 'years':
                    start = datetime(year, month, day)
                    end = datetime(year + value, month, day) - timedelta(days=1)
                    result += end - start

                elif key == 'months':
                    # figure out how many whole years and left over months and
                    # then let pythons datetime do all the work
                    years = value / 12
                    months = value % 12
                    start = datetime(year, month, day)
                    end = datetime(year + years, month + months, day)
                    result += end - start

                elif key == 'weeks':
                    result += timedelta(weeks=value)

                elif key == 'days':
                    result += timedelta(days=value)

                elif key == 'hours':
                    result += timedelta(hours=value)

                elif key == 'minutes':
                    result += timedelta(minutes=value)

                elif key == 'seconds':
                    result += timedelta(seconds=value)

        return result
