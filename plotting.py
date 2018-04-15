#!/usr/bin/env python3
# Zachary Zwierko, 04/14/2018

from analyze import *

ROW_N = 500000

def compare(x, y, plot=True, title=None, xlabel=None, ylabel=None):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

    sample1 = random_n(ROW_N)[[x, y]].dropna()
    sample2 = random_n(ROW_N)[[x, y]].dropna()
    sample3 = random_n(ROW_N)[[x, y]].dropna()
    sample4 = random_n(ROW_N)[[x, y]].dropna()

    sns.regplot(x=x, y=y, data=sample1, ax=ax1)
    sns.regplot(x=x, y=y, data=sample2, ax=ax2)
    sns.regplot(x=x, y=y, data=sample3, ax=ax3)
    sns.regplot(x=x, y=y, data=sample4, ax=ax4)

    plt.xlabel(xlabel or x)
    plt.ylabel(ylabel or y)
    plt.show()

compare("estimatedSalary", "clicks")