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

def random_n(num_rows):
    return pd.read_sql(f"""
SELECT *
FROM jobs
WHERE jobid IN (SELECT jobid
                FROM jobs
                ORDER BY RANDOM()
                LIMIT {num_rows})
""", conn)

conn = sqlite3.connect("data/indeed.db")

jobs = random_n(100000)
jobs.replace("", np.nan, inplace=True)