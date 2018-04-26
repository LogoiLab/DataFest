#!/usr/bin/env python3

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from analyze import *

distinct_titles = query_db("SELECT DISTINCT normTitle FROM jobs")
test_vals = query_db(f"SELECT estimatedSalary from jobs limit 50")
print(test_vals.mean())
print(test_vals.std())
random_sals = np.random.normal(test_vals.mean(), test_vals.std(), 50)


def classify(title, salary):
    matches = test_data
    matches = matches[matches["normTitle"] == title]
    matches = matches[matches["estimatedSalary"].between(salary-5000, salary+5000, inclusive=True)]
    match = matches[matches["clicks"] == matches["clicks"].max()]
    return match


match_list = pd.DataFrame()
test_data = random_n(50)

for sal in random_sals:
    match_list.append(classify(distinct_titles.sample(n=1), sal))

print(match_list.head())
print(match_list.tail())

match_list = match_list[['normTitle', 'clicks', 'estimatedSalary']]

with plt.xkcd():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    for row in axes:
        for ax in row:
            sample = match_list

            _, pval = pearsonr(sample['estimatedSalary'], sample['clicks'])

            sns.regplot(x='estimatedSalary', y='clicks', data=sample,
                        ax=ax, fit_reg=False, scatter_kws={"s": 1}, marker=".")

            ax.text(0.5, 0.5, f"p-value: {pval:.4f}", transform=ax.transAxes, fontsize=10)

            plt.title('Best Clicks per Salary')
            plt.xlabel('Salary')
            plt.ylabel('Clicks')

        plt.savefig(f"plot{random.randint(0, 10000)}.png")
