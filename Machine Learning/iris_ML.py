import sklearn
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plotear_puntos_columnas(columna1,columna2):
    plt.figure(figsize=(5, 4))

    plt.scatter(X[:50, columna1], X[:50, columna2],
                color='blue', marker='o', label='Setosa')
    plt.scatter(X[50:100, columna1], X[50:100, columna2],
                color='green', marker='s', label='Versicolor')
    plt.scatter(X[100:150, columna1], X[100:150, columna2],
                color='red', marker='s', label='Virginica')
    return

def plotear():
    # plot data SEPALO
    plotear_puntos_columnas(0,1)

    plt.title('Sepalo')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.legend(loc='upper left')
    
    plt.show()

    # plot data PETALO
    plotear_puntos_columnas(2,3)

    plt.title('Petalo')
    plt.xlabel('Petal length')
    plt.ylabel('Petal width')
    plt.legend(loc='upper left')
    
    plt.show()

    # plot data LONGITUD
    plotear_puntos_columnas(0,2)

    plt.title('Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.legend(loc='upper left')
    
    plt.show()

    # plot data ANCHURA
    plotear_puntos_columnas(1,3)

    plt.title('Width')
    plt.xlabel('Sepal Width')
    plt.ylabel('Petal Width')
    plt.legend(loc='upper left')
    
    plt.show()

def mapas_orrelacion(iris):
    #gives positive & negative relation between categories
    import seaborn as sns
    sns.heatmap(iris.corr(), annot=True)
    plt.show()

    #Correlation chart on different variables for comparision
    sns.pairplot(iris)
    plt.show()

def knn_comparison(X,y, k):
    # Visualising the Training set results
    import matplotlib.pyplot as plt
    from sklearn import neighbors

    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(X, y)
    # Plotting decision region
    plot_decision_regions(X, y, clf=clf, legend=2)
    # Adding axes annotations
    plt.title("K-NN (Training set)")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Knn with K="+ str(k))
    plt.show()

def precision(y_test, y_pred):
    
    # Calculo de precisión del modelo
    from sklearn.metrics import precision_score
    precision = precision_score(y_test, y_pred, average='macro')
    print("Precisión del modelo:")
    print(precision)

    from sklearn.metrics import accuracy_score
    exactitud = accuracy_score(y_test, y_pred)
    print("Exactitud del modelo:")
    print(exactitud)

    # Calcular la sensibilidad del modelo
    from sklearn.metrics import recall_score
    sensibilidad = recall_score(y_test, y_pred, average='macro')
    print("Sensibilidad del modelo")
    print(sensibilidad)

    #Calculo el puntaje F1 del modelo
    from sklearn.metrics import f1_score
    puntajef1 = f1_score(y_test, y_pred, average='macro')
    print("Puntaje F1 del modelo")
    print(puntajef1)


iris=pd.read_csv("C://Users/cjcue/Documents/GitHub/DataScience/media/iris.csv")


# Transformamos los datos de species en numeros

iris['species']=iris['species'].map({"setosa":0, "versicolor":1, "virginica":2}).astype(int)
samples=iris.sample(10)
print(samples)
quit()
#iris.drop(['species'], axis=1, inplace=True)

iris = iris.iloc[0:150, :]

# Supervised Learning: Classification and regression
# KNN classifier
from sklearn import neighbors, datasets
X= iris.iloc[:, 0:4].values #petal_length
y= iris.species.values

# Seleccionamos los datos de test y entrenamiento
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Escalamos los datos
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()

X_train = escalar.fit_transform(X_train)
X_test = escalar.fit_transform(X_test)

#Defino el algoritmo a utilizar
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# SOLO VALIDO PARA 2 VARIABLES EN X
# for i in [1,2,3,4,5,6]:
#     knn_comparison(X, y, i)

# Imprimimos precision del modelo

precision(y_test, y_pred)

####-Means Clustering
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1, 12))
visualizer.fit(iris)
visualizer.show()

kmeans = KMeans(n_clusters=3, init="k-means++", random_state=0).fit(iris)

import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue=kmeans.labels_, cmap ='rainbow')
plt.show()

# Hierarchical Clustering
X= iris.petal_length
y= iris.petal_width
data = list(zip(X, y))


from scipy.cluster.hierarchy import dendrogram, linkage
linkage_data = linkage(data, method="ward", metric="euclidean")
dendrogram(linkage_data)
plt.show()

# Aglomerativas
from sklearn.cluster import AgglomerativeClustering
hierarchical = AgglomerativeClustering(n_clusters=4, affinity="euclidean", linkage="ward")
labels= hierarchical.fit_predict(data)

plt.scatter(X, y, c=labels)
plt.show()


