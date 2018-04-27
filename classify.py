#!/usr/bin/env python3

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import random

from analyze import *


distinct_titles = query_db("SELECT DISTINCT normTitleCategory FROM jobs")
test_vals = query_db("SELECT estimatedSalary from jobs limit 5000")
print(test_vals.mean())
print(test_vals.std())
random_sals = np.random.normal(test_vals.mean(), test_vals.std(), 2000000)


def classify(title, salary):
    matches = test_data
    matches = matches[matches["normTitleCategory"] == title]
    matches = matches[matches["estimatedSalary"].between(salary-5000, salary+5000, inclusive=True)]
    match = matches[matches["clicks"] == matches["clicks"].max()]
    return match


match_list = pd.DataFrame()
test_data = random_n(2000000)

for sal in random_sals:
    match_list = match_list.append(classify(str(distinct_titles.sample(n=1).iloc[0][0]), sal))

print(match_list.head())
print(match_list.tail())

with plt.xkcd():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    for row in axes:
        for ax in row:
            sample = match_list

            _, pval = pearsonr(sample['estimatedSalary'], sample['clicks'])

            g = sns.regplot(x='estimatedSalary', y='clicks', data=sample,
                        ax=ax, fit_reg=False, scatter_kws={"s": 1}, marker=".")

            ax.text(0.5, 0.5, "p-value: {:.4f}".format(pval), transform=ax.transAxes, fontsize=10)

            g.set_title('Best Clicks per Salary')
            plt.xlabel('Salary')
            plt.ylabel('Clicks')

        plt.savefig(f"plot{random.randint(0, 10000)}.png")
