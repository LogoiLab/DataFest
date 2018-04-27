#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:38:59 2018

@author: David
"""

from analyze import *
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import ensemble 

jobs.dropna(axis = 0)
# "normTitle", "normTitleCategory",  "normTitle","educationRequirements", "stateProvince", "city","country", 
print(len(jobs))

#jobs2 = jobs[["estimatedSalary", "licenseRequiredJob","supervisingJob"]]

#print(jobs['normTitleCategory'].value_counts())

jobs2 = jobs[['normTitleCategory', 'clicks', 'stateProvince', 'estimatedSalary']]

jobs2 = jobs2.loc[jobs2['stateProvince'].str.contains('VA')]
#print(pd.crosstab(jobs2.normTitleCategory, jobs2.stateProvince))

salary = jobs2['estimatedSalary'].median()

things = jobs.groupby(['stateProvince'])['estimatedSalary'].median()

things2 = jobs.groupby(['normTitleCategory'])['estimatedSalary'].median()
titles = jobs.normTitleCategory.unique()

xy = zip(titles,things)
second = sorted(xy, key=lambda tup: tup[1])
print(list(second))
#sorted(things2)

list1 = ['care', 'food', 'retial', 'warehouse', 'hospitality','meddr', 'techsoftware', 'engid', 'engmech', 'engcivil', 'engelectric']
list2 = [22300, 22300, 22800, 23100, 25500, 136100, 97200, 85300, 81200, 78300, 78300]

salaries = pd.DataFrame({'job':list1, 'expectedSalary':list2})

#tings2 = sorted(jobs['stateProvince'])
#sns.barplot(things)
#data_y = jobs["experienceRequired"]
#pd.crosstab(index = columns = jobs['normTitleCategory'], margins = True)
#print(jobs.head())
#stuff = pd.get_dummies(jobs2, columns=["stateProvince","country", "city"])

#jobs = jobs.drop("jobLanguage")
#sns.countplot(data = jobs, x = "country")
#sns.regplot(y = "estimatedSalary", x = "experienceRequired", data = jobs, )
#plt.show()
#data_y = stuff["normTitleCategory"]
#sns.regplot(x = "clicks", y= "localClicks", data = jobs)
#plt.yscale("log")
#plt.xscale("log")

