import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from sklearn import datasets, metrics
from sklearn.svm import SVC

# Load the iris datasets
ds = datasets.load_iris()
# fit a SVM model to the data
model = SVC()
model.fit(ds.data, ds.target)
# print(model)
# print(ds)

# make predictions
expected = ds.target
predicted = model.predict(ds.data)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
