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
                                   where country = 'US'
                                   ORDER BY RANDOM()
                                   LIMIT {num_rows})
                      
                """, conn)
    ret.replace("", np.nan, inplace=True)
    return ret

def query_db(query_str):
    return pd.read_sql(query_str, conn)

conn = sqlite3.connect("data/indeed.db")

jobs = random_n(10000)
jobs.replace("", np.nan, inplace=True)

