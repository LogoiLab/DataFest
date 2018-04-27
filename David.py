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

# "normTitle", "normTitleCategory",  "normTitle","educationRequirements", "stateProvince", "city","country", 


jobs2 = jobs[["estimatedSalary", "licenseRequiredJob","supervisingJob"]]

data_y = jobs["experienceRequired"]

print(jobs.head())
#stuff = pd.get_dummies(jobs2, columns=["stateProvince","country", "city"])

#jobs = jobs.drop("jobLanguage")
#sns.countplot(data = jobs, x = "country")

#sns.regplot(y = "estimatedSalary", x = "experienceRequired", data = jobs, )
#plt.show()

#data_y = stuff["normTitleCategory"]

sns.regplot(x = "clicks", y= "estimatedSalary", data = jobs)


