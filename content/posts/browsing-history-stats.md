---
title: "Getting stats on browsing history from the browser database"
date: 2020-09-18
category: "programming"
tags: ["python", "open data", "coding"]
slug: "browsing-stats"
---

If you didn't know, there are more SQLite databases in the universe ([1+ trillion](https://www.sqlite.org/mostdeployed.html)) than there are known galaxies ([100 billion](https://www.discovermagazine.com/the-sciences/how-many-galaxies-are-there-astronomers-are-revealing-the-enormity-of-the)). And one of those SQLite databases happens to be your browsing history. As a short proof-of-concept, here's how to access the history of your Firefox browser via the SQLite database.

## find your database file

Mozilla Firefox stores your cookies, bookmarks, form inputs, and browsing history under the path defined in your profile settings. To find the path of those files in your file system, visit **about:profiles** in a Firefox window.

In my case, I only use really one profile, which is shown in the orange box.

![showing file system path to profile in firefox](/images/firefox-profile-path.png)

You can click "Show in Finder" and then scroll down to the file `places.sqlite`. Trying to directly open this database file gives the error "locked database" -- you'll need to make a copy of the file in a different folder before opening.

![database is locked](/images/firefox-db-locked.png)

## explore the database

The go-to SQLite client is [DB Browser for SQLite](https://sqlitebrowser.org/). Once installed, you can easily open your `places.sqlite` file with "Open With" from Finder.

![opening the db file](/images/firefox-db-openwith.png)

Once the database file is open, you'll see 13 tables

![finding the right tables](/images/firefox-db-tables.png)

After digging through a couple tables, the one with your browsing history is called `moz_places`. By viewing this table, you'll see that the field `url` stores the page visited, and last visit date is the UNIX timestamp of the last visit.

![viewing the table with browsing history](/images/firefox-db-history-view.png)

Sort descending by `visit_count` and you'll find your most commonly viewed website. For me, it's HackerNews, and then various permutations of Twitter. (I use the mobile Twitter site instead of the app, and I sync my history between devices.)

## query the database

Despite using Twitter, I'm a private person, and I don't want to share any real analysis of my browsing history. I do want to share one result: the distribution of `http://localhost` ports. Here's a short python3 script that reads the copy of the `place.sqlite` file, and returns a count of localhost ports from the browsing history.

```python
import pandas as pd
import sqlite3

# connect and read database
con = sqlite3.connect('places.sqlite')
df = pd.read_sql_query('select * from moz_places', con)
con.close()

# filter for urls containing localhost
# notice I include ':', which means a port should be defined
df = df[df.url.str.contains('localhost:',case=False)]

# parse the url to get just the port
df.port = df.url.str.split(':').str[-1].str.split('/').str[0]

# keep only port column and do a count by grouping each port
df = df.port
df = df.groupby(df).count()

print(df.to_markdown())
```

Here's the results, with my annotation:

| port  | count | description                                    |
|:------|:-----:|:-----------------------------------------------|
| 1313  | 144   | Hugo devserver - this site!                    |
| 3000  | 41    | Metabase (?), which I tested a while ago       |
| 5000  | 4     | Flask web server (work stuff)                  |
| 50222 | 1     | Callback for Tableau authentication            |
| 58595 | 1     | Not sure, but probably similar to  50222       |
| 8000  | 137   | Old faithful, in this case mkdocs (work stuff) |
| 8888  | 37    | Jupyter notebook server                        |
| 8889  | 4     | Jupyter notebook server                        |
| 9005  | 1     | Callback for Firebase CLI authentication       |
|       | 7     | No port means URL had multiple `:`. See below. |


Similar aggregation could be done directly in SQL:

```sql
select
   port,
   count(1) 
from
   (
      select
         url,
         replace( replace( substr(url, instr(url, 'localhost:'), 15), 'localhost:' , ''), '/', '') as port 
      from
         moz_places 
      where
         url like '%localhost:%' 
   )
group by
   port
```

which generates _almost_ identical results.

The SQL query picked up one instance of `localhost:9005` that the Python script didn't find. 

Digging deeper:

```sql
select
   * 
from
   moz_places 
where
   url like '%localhost:9005%'
```

shows that port 9005 was used for the Callback on Firebase CLI authentication. The reason is because the Python script splits on the `:` character, for which this URL has more than one. The table shows 7 localhost URLs without ports, but these are actually URLs that have more than one `:` character. I've updated the table above, but not the Python script.

## conclusion

Everything is a SQLite database.