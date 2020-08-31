---
title: "Generating folders with smart dates in Python + Pandas"
date: 2020-08-31
category: "programming"
tags: ["python", "coding"]
slug: "python-date-folders"
---

> _Not everything your mother told you is true._

<small>--my CompSci 101 professor, when a student _insisted_ that, without exception, every 4th year was a leap year</small>

---

### the idea

For a hobby project, I needed to generate thousands folders and sub-folders and sub-sub-folders based on calendar dates within a range.

This means, I wanted to have a main folder, called something like `tmp_dates/`. In that folder, I wanted to have sub-folders for each year within a range: `tmp_dates/2020/`. And sub-folders for months: `tmp_dates/2020/06/`. And sub-folders for days: `tmp_dates/2020/06/30`.

### smart calendar dates and leap years

Using Python's standard `datetime` library, I can easily generate date ranges with `timedelta()`. This is necessary for generating "smart"-dates that take into account varying days per month, as well as those pesky leap years. It turns out that the [rules for leap years](https://en.wikipedia.org/wiki/Leap_year#Algorithm) are **not** as simple as years that are multiples of 4. <small>Sadly, for those of us born in the late 20th Century, we won't be alive to see a year divisible by 4 that is _not_ a leap year. The next one of those is year `2100`. The year `2000` was a leap year despite being divisible by 100 because it was also divisible by 400.</small>

Wrapping the date-range functionality with Pandas makes the code extremely efficient. Here's an adapted [StackOverflow snippet](https://stackoverflow.com/a/59882807/2327328) which does the heavy lifting. 

```python
import pandas as pd
from datetime import date, timedelta
sdate = date(2000,1,1)   # start date
edate = date.today() # end date
df = pd.date_range(sdate,edate-timedelta(days=1),freq='d')
```

### generating (sub-)folders based on a date range

In addition to generating the date-folders, I want my code to create folders but not overwrite files if a folder exists. For this I used [this snippet](https://stackoverflow.com/a/273227/2327328) that uses the wonderful new Python3 library [`pathlib.Path()`](https://docs.python.org/3/library/pathlib.html) to create a folder called `tmp_dates/` in the current working directory. If that folder already exists, it will otherwise ignored.

```python
from pathlib import Path
Path('tmp_dates/').mkdir(parents=True, exist_ok=True)
```

### adding an empty file to each folder

Git can't handle an empty directory. To include empty directories, on Github at least, there is an [undocumented feature](https://stackoverflow.com/a/7229996/2327328) where an empty folder that has the empty file `.gitkeep` will be included in the version control. The `pathlib.Path()` library can even create an empty file, using the [`.touch()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.touch) function, which copies its functionality from the [Unix touch command](https://en.wikipedia.org/wiki/Touch_(command)#Overview).

```python
from pathlib import Path
Path('tmp_dates/').mkdir(parents=True, exist_ok=True)
Path('tmp_dates/'+os.sep+'.gitkeep').touch()
```

### putting it all together

All that's left is to combine all the pieces into one Python3 script that safely generates sub-folders for individual calendar dates in a date range.

```python
from datetime import date, timedelta
import pandas as pd
from pathlib import Path #requires Python>=3.5
import os

# safe generate folders for all dates within a range
def create_folder(p):
    Path(p).mkdir(parents=True, exist_ok=True)
    Path(p+os.sep+'.gitkeep').touch()

# where to start to put the many folders
subpath = 'tmp_dates'

# start and end date
sdate = date(2000,1,1)   # start date
edate = date.today() # end date

# use pandas for the heavy lifting of building the calendar-aware date range
df = pd.date_range(sdate,edate-timedelta(days=1),freq='d')

# loop over all values and create a folder for each possible date
for d in df:
    #print(d.year, d.month, d.day)
    path = subpath + os.sep + str(d.year).zfill(4) + os.sep + str(d.month).zfill(2) + os.sep + str(d.day).zfill(2)
    create_folder(path)
    #break # debugging
```
