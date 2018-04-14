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
    return pd.read_sql(f"""
SELECT *
FROM jobs
LIMIT {num_rows}
""", conn)

conn = sqlite3.connect("data/indeed.db")

jobs = random_n(5000000)
jobs.replace("", np.nan, inplace=True)