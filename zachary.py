# Zachary Zwierko, 04/14/2018

from analyze import *

# Better description == better review?
q2 = data[["descriptionWordCount", "numReviews"]]
q2 = q2.dropna()