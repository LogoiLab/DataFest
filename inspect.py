#!/usr/bin/env python3
"""
Chad Baxter, David Zamojda, Zachary Zwierko
DataFest
Spring 2018
"""

import sqlite3

with sqlite3.connect("data/indeed.db") as conn:
    cur = conn.cursor()

