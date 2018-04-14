import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import keras

from keras import models
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics
from keras.models import Sequential
from keras.layers import Dense

from sklearn.cross_validation import train_test_split

from analyze import *

jobs = random_n(500000)
jobs = jobs[['clicks', 'localClicks', 'avgOverallRating']]
jobs = jobs.dropna()

features_train, features_test, target_train, target_test = train_test_split(jobs[['clicks', 'localClicks']], jobs["avgOverallRating"], test_size=.3, random_state=100)

model = Sequential()

model.add(layers.Dense(2, activation='relu', input_dim=2))
model.add(layers.Dense(1, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
              loss=losses.binary_crossentropy,
              metrics=[metrics.binary_accuracy])

model.fit(features_train, target_train, epochs=5)

scores = model.evaluate(features_test, target_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

