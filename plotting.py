#!/usr/bin/env python3
# Zachary Zwierko, 04/26/2018

import argparse
import random

from scipy.stats import pearsonr

from analyze import *

ROW_N = 500000

def is_numeric(colname):
    result = conn.execute(f"""
SELECT {colname}
FROM jobs
WHERE {colname}
LIMIT 1
""").fetchone()

    if result:
        try:
            float(result[0])
        except (TypeError, ValueError):
            return False
        return True
    return False

def compare(col1, col2):
    col1_num = is_numeric(col1)
    col2_num = is_numeric(col2)

    with plt.xkcd():
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        for row in axes:
            for ax in row:
                sample = random_n(ROW_N)[[col1, col2]].dropna()

                if not col1_num and col2_num:
                    sns.violinplot(x=col1, y=col2, data=sample, ax=ax, orient="vertical")
                    ax.set_xticks([])
                    plt.xlabel(col1)
                    plt.ylabel(col2)
                elif col1_num and not col2_num:
                    sns.violinplot(x=col2, y=col1, data=sample, ax=ax, orient="vertical")
                    ax.set_xticks([])
                    plt.xlabel(col2)
                    plt.ylabel(col1)
                elif not col1_num and not col2_num:
                    sns.countplot(x=col1, data=sample)
                    sns.countplot(x=col2, data=sample)
                    plt.xlabel(col1)
                    plt.ylabel(col2)
                else:
                    _, pval = pearsonr(sample[col1], sample[col2])

                    sns.regplot(x=col1, y=col2, data=sample,
                                ax=ax, fit_reg=False, scatter_kws={"s": 1}, marker=".")
                    plt.xlabel(col1)
                    plt.ylabel(col2)

                    ax.text(0.5, 0.5, f"p-value: {pval:.4f}", transform=ax.transAxes, fontsize=10)

        plt.savefig(f"plot{random.randint(0, 10000)}.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="plotting.py")
    parser.add_argument("-i", "--important")
    parser.add_argument("-t", "--test", nargs="+")

    args = parser.parse_args()

    for test in args.test:
        compare(args.important, test)
