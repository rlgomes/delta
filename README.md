# delta

[![Build Status](https://travis-ci.org/rlgomes/delta.svg?branch=master)](https://travis-ci.org/rlgomes/delta)

Human friendly context aware duration parsing library that can translate
expressions such as '1 hour' to a [timedelta](https://docs.python.org/2/library/datetime.html#datetime.timedelta)
object. The context aware notion comes from the ability to parse a duration
of months or years but taking into account the current date (ie context) from
where to start calculating the delta.

# installation

## from pypi

```
pip install delta
```

## from source

```
pip install -e git+git://github.com/rlgomes/delta.git#egg=delta
```

# usage

## syntax

*delta* only exports a single `parse()` function that accepts a duration
string and returns the `timedelta` object that duration represents. The duration
expression consists of a number followed by a unit and separated by a comma, space
or 'and' keyword. So the following are valid duration expression:

```
1 year 2 months and 3 weeks
2 months, 3 weeks and 12 days
1y 2m 3w 4d
3.5 years and 2.7 days
```

Units include:

 * y, year, years
 * m, month, months
 * w, week, weeks
 * d, day, days
 * h, hour, hours
 * min, minute, minutes
 * s, second, seconds
 * ms, millis, millisecond, milliseconds

## code sample

```python
import delta

tdelta = delta.parse('1 day')
```

Context aware parsing that can calculate months and years based on the datetime
object provided as context:

```python
import delta
from datetime import datetime

tdelta = delta.parse('2 months', context=datetime(2016, 1, 1))
```

The above delta calculated will take into account that the `context` is set to
the first day of 2016 which means 2 months is 31 days from January and 29 days
from February.

## tests

Tests can be run using [tox](http://tox.testrun.org).

```
pip install tox
tox
```
