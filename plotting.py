#!/usr/bin/env python3
# Zachary Zwierko, 04/14/2018

import random

from scipy.stats import pearsonr

from analyze import *

ROW_N = 500000

def compare(x, y, is_cat=False, title=None, xlabel=None, ylabel=None):
    with plt.xkcd():
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        for row in axes:
            for ax in row:
                sample = random_n(ROW_N)[[x, y]].dropna()

                if is_cat:
                    sns.violinplot(x=x, y=y, data=sample,
                                   ax=ax, orient="vertical")
                    ax.set_xticks([])
                else:
                    _, pval = pearsonr(sample[x], sample[y])

                    sns.regplot(x=x, y=y, data=sample,
                                ax=ax, fit_reg=False, scatter_kws={"s": 1}, marker=".")

                    ax.text(0.5, 0.5, f"p-value: {pval:.4f}", transform=ax.transAxes, fontsize=10)

                if title:
                    plt.title(title)
                plt.xlabel(xlabel or x)
                plt.ylabel(ylabel or y)

        plt.savefig(f"plot{random.randint(0, 10000)}.png")

compare("stateProvince", "clicks", is_cat=True)
compare("city", "clicks", is_cat=True)
compare("avgOverallRating", "clicks")
compare("numReviews", "clicks")
compare("descriptionWordCount", "clicks")
compare("experienceRequired", "clicks")
compare("jobLanguage", "clicks", is_cat=True)
compare("supervisingJob", "clicks", is_cat=True)
compare("licenseRequiredJob", "clicks", is_cat=True)
compare("educationRequirements", "clicks", is_cat=True)
compare("jobAgeDays", "clicks")
compare("localClicks", "clicks")
