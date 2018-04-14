#!/usr/bin/env python3
"""
Chad Baxter, David Zamojda, Zachary Zwierko
DataFest
Spring 2018
"""

import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def random_n(num_rows):
    ret = pd.read_sql(f"""
SELECT *
FROM jobs
WHERE id IN (SELECT id
             FROM jobs
             ORDER BY RANDOM()
             LIMIT {num_rows})
""", conn)
    ret.replace("", np.nan, inplace=True)
    return ret

conn = sqlite3.connect("data/indeed.db")
