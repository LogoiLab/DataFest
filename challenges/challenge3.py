import datetime
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect("../data/indeed.db")

data = pd.read_sql(f"""
SELECT date, clicks, normTitleCategory
FROM jobs
WHERE normTitleCategory IN ("management", "admin", "sales", "retail", "techsoftware")
""", conn)

d1 = data[data["normTitleCategory"] == "management"][["date", "clicks"]]
d2 = data[data["normTitleCategory"] == "admin"][["date", "clicks"]]
d3 = data[data["normTitleCategory"] == "sales"][["date", "clicks"]]
d4 = data[data["normTitleCategory"] == "retail"][["date", "clicks"]]
d5 = data[data["normTitleCategory"] == "techsoftware"][["date", "clicks"]]

d1["date"] = pd.to_datetime(d1["date"])
d1.set_index("date", inplace=True)
d1 = d1.groupby(pd.Grouper(freq="M")).sum()

d2["date"] = pd.to_datetime(d2["date"])
d2.set_index("date", inplace=True)
d2 = d2.groupby(pd.Grouper(freq="M")).sum()

d3["date"] = pd.to_datetime(d3["date"])
d3.set_index("date", inplace=True)
d3 = d3.groupby(pd.Grouper(freq="M")).sum()

d4["date"] = pd.to_datetime(d4["date"])
d4.set_index("date", inplace=True)
d4 = d4.groupby(pd.Grouper(freq="M")).sum()

d5["date"] = pd.to_datetime(d5["date"])
d5.set_index("date", inplace=True)
d5 = d1.groupby(pd.Grouper(freq="M")).sum()

plt.plot(d1.index, d1["clicks"], label="Management")
plt.plot(d2.index, d2["clicks"], label="Admin")
plt.plot(d3.index, d3["clicks"], label="Sales")
plt.plot(d4.index, d4["clicks"], label="Retail")
plt.plot(d5.index, d5["clicks"], label="Tech Software")

plt.title("Data Challenege #3")
plt.xlabel("Date")
plt.ylabel("Total clicks")

plt.xlim([datetime.date(2016, 10, 31), datetime.date(2018, 1, 1)])

plt.legend()
plt.show()
