#!/usr/bin/env python3
"""
Chad Baxter, David Zamojda, Zachary Zwierko
DataFest
Spring 2018
"""

import sqlite3

import pandas as pd

with sqlite3.connect("data/indeed.db") as conn:
    cur = conn.cursor()

    jobs = cur.execute("""
SELECT *
FROM jobs
LIMIT 100000
""")

    names = [x[0] for x in cur.description]
    rows = jobs.fetchall()

data = pd.DataFrame(rows, columns=names)