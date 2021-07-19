import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
diabetesDataSet = pd.read_csv("pima-indians-diabetes.csv")
print(diabetesDataSet)

featureColumns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']

X = diabetesDataSet[featureColumns]
Y = diabetesDataSet.label

print("~~~~~~~~~FEATURES~~~~~~~~~~")
print(X)
print("~~~~~~~~~LABELS~~~~~~~~")
print(Y)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

print(">> Accuracy Score:", metrics.accuracy_score(y_test, y_pred))