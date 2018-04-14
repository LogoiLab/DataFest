#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:38:59 2018

@author: David
"""

from analyze import *
import matplotlib.pyplot as plt

states = jobs[["stateProvince", "city", "country", "industry", "normTitle", "experienceRequired", "estimatedSalary"]]
sns.countplot(data = jobs, x = "country")


