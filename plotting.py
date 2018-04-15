#!/usr/bin/env python3
# Zachary Zwierko, 04/14/2018

from scipy.stats import pearsonr

from analyze import *

ROW_N = 500000

def compare(x, y, title=None, xlabel=None, ylabel=None):
    with plt.xkcd():
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        for row in axes:
            for ax in row:
                sample = random_n(ROW_N)[[x, y]].dropna()

                _, pval = pearsonr(sample[x], sample[y])

                sns.regplot(x=x, y=y, data=sample,
                            ax=ax, fit_reg=False, scatter_kws={"s": 1}, marker=".")
                ax.text(0.5, 0.5, f"p-value: {pval:.3f}", transform=ax.transAxes, fontsize=10)

                plt.title(title)
                plt.xlabel(xlabel or x)
                plt.ylabel(ylabel or y)

        plt.show()

compare("estimatedSalary", "clicks")