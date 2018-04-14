#!/usr/bin/env python3
"""
Chad Baxter, David Zamojda, Zachary Zwierko
DataFest
Spring 2018
"""

import sqlite3

import numpy as np
import pandas as pd
import seaborn as sns

with sqlite3.connect("data/indeed.db") as conn:
    cur = conn.cursor()

    jobs = cur.execute("""
SELECT *
FROM jobs
LIMIT 1000000
""")

    names = [x[0] for x in cur.description]
    rows = jobs.fetchall()

data = pd.DataFrame(rows, columns=names)
data.replace('', np.nan, inplace=True)
data = data.dropna()

def random_n(num_rows):
    return pd.read_sql("SELECT * FROM jobs WHERE id IN (SELECT id FROM jobs ORDER BY RANDOM() LIMIT " + str(num_rows) + ")", conn)

