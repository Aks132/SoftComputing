# Kick off by importing libraries, and outlining the Iris dataset
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler  
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import classification_report, confusion_matrix 

url = open("iris.csv", "r")
url.read()

# Let's start by naming the features
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Reading the dataset through a Pandas function
irisdata = pd.read_csv("iris.csv", names=names)

# Takes first 4 columns and assign them to variable "X"
X = irisdata.iloc[:, 0:4]
# Takes first 5th columns and assign them to variable "Y". Object dtype refers to strings.
y = irisdata.select_dtypes(include=[object])

X.head()
y.head()

# y actually contains all categories or classes:
y.Class.unique()
le = preprocessing.LabelEncoder()
y = y.apply(le.fit_transform)

y.head()

# Now for train and test split (80% of  dataset into  training set and  other 20% into test data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


# Feature scaling
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# Finally for the MLP- Multilayer Perceptron
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train.values.ravel())


predictions = mlp.predict(X_test)

print(predictions)

# Last thing: evaluation of algorithm performance in classifying flowers
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))