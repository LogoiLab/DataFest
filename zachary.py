#!/usr/bin/env python3
# Zachary Zwierko, 04/14/2018

from sklearn.preprocessing import MinMaxScaler

from analyze import *

min_max_scaler = MinMaxScaler()

# Better description == better review?
q2 = jobs[["descriptionWordCount", "numReviews"]]
q2 = q2.dropna()

q2 = pd.DataFrame(min_max_scaler.fit_transform(q2.values))

sns.regplot("descriptionWordCount", "numReviews", data=jobs, fit_reg=False, scatter_kws={"s": 1})
plt.show()

# Can you tell how highly rated a company is from clicks?
# q4 = jobs[["avgOverallRating", "clicks"]]
# q4 = q4.dropna()
# sns.regplot("descriptionWordCount", "numReviews", data=jobs)
# plt.show()