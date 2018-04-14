#!/usr/bin/env python3
# Zachary Zwierko, 04/14/2018

from analyze import *

ROW_N = 1000000

jobs = random_n(ROW_N)
jobs = jobs.dropna()

# Better description == better review?
def q2():
    with plt.xkcd():
        plt.figure()
        sns.jointplot("descriptionWordCount", "numReviews",
                      data=jobs, kind="reg")
        plt.xlim(0, jobs["descriptionWordCount"].max())
        plt.ylim(0, jobs["numReviews"].max())

def q4():
    with plt.xkcd():
        plt.figure()
        sns.jointplot("avgOverallRating", "clicks",
                      data=jobs, kind="reg")
        plt.xlim(0, jobs["avgOverallRating"].max())
        plt.ylim(0, jobs["clicks"].max())

def t1():
    with plt.xkcd():
        plt.figure()
        sns.regplot("estimatedSalary", "clicks", data=jobs)
if __name__ == "__main__":
   t1()

   plt.show()