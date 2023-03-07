import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("train.csv")
data = data.to_numpy()
clf=DecisionTreeClassifier()

xtrain=data[0:21000,1:]
train_label=data[0:21000,0]

clf.fit(xtrain,train_label)

xtest=data[21000:,1:]
actual_label=data[21000:,0]

d=xtest[20]
d.shape=(28,28)
plot.imshow(255-d,cmap='gray')
print(clf.predict([xtest[20]]))
plot.show()