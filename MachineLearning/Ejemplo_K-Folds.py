from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

import pandas as pd

iris = datasets.load_iris()

#### cargamos todos los datos de un dataframe
df= pd.DataFrame(iris.data, columns=['sepal_length', 'sepal_width','petal_length',  'petal_width'])

Tipo_iris = iris.target
df["Tipo_iris"]=Tipo_iris

df['Tipo_iris']=df['Tipo_iris'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

#### modelo entrenamiento

# Seleccionamos un 20% los registros de test
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

# vamos a hacer 5 iteraciones del modelo
kf = KFold(n_splits=5)

# vamos a hacer la iteracion con un solo modelo, el de regresion logistica
clf = LogisticRegression()

# entrenamos el modelo 
clf.fit(X_train, y_train)

# Obtenemos el score del modelo de entrenamiento
score = clf.score(X_train,y_train)

# Hacemos el Cross 5 veces del modelo de regresion logistica y obtenemos los scores
scores = cross_val_score(clf, X_train, y_train, cv=kf, scoring="accuracy")


# Calculamos cual es el resultado de la prediccion "y_pred" del test
preds = clf.predict(X_test)

# Calculamos el score del modelo testado
score_pred = metrics.accuracy_score(y_test, preds)

print("Metrica del modelo", score)
print("Metricas cross_validation", scores)
print("Media de cross_validation", scores.mean())
print("Metrica en Test", score_pred)

#######