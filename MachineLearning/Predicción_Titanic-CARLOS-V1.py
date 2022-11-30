# Titanic Dataset - Predicción
# Para competir en Kaggle será necesario descargar de esta página los csv de: train.csv, test.csv, gender_submission.csv 
# https://www.kaggle.com/competitions/titanic/data


import pandas as pd
import numpy as np

# importamos algoritmos
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

import string
import warnings
warnings.filterwarnings('ignore')

# Feature Engineering
# En esta parte podemos hacer uso de la información obtenida y conclusiones.
# Para hacerlo lo más simple posible, lo que haremos será elegir solamente algunas columnas.


def concat_df(train_data, test_data):
    # Returns a concatenated df of training and test set
    test_data["Origen"]="test"
    train_data["Origen"]="train"
    df=pd.concat([train_data, test_data], sort=True).reset_index(drop=True)
    return df

def separar_df(df, train_data, test_data):
    # Separa el df en el train y el test
    groups = df.groupby(df.Origen)
    test_data = groups.get_group("test")
    train_data = groups.get_group("train")
    test_data = test_data.drop(["Origen","Survived"], axis=1)
    train_data = train_data.drop(["Origen"], axis=1)

    return train_data, test_data

def Correlaciones(df):
    df.name = "All Set"

    df_corr = df.corr().abs().unstack().sort_values(kind="quicksort", ascending=False).reset_index()
    df_corr.rename(columns={"level_0": "Feature 1", "level_1": "Feature 2", 0: 'Correlation Coefficient'}, inplace=True)
    df_corr[df_corr['Feature 1'] == 'Age']
    print(df_corr[df_corr['Feature 1'] == 'Age'])
    return


def Name(df):
    df['Title'] = df['Name'].str.split(', ', expand=True)[1].str.split('.', expand=True)[0]
    df['Is_Married'] = 0
    df['Is_Married'].loc[df['Title'] == 'Mrs'] = 1
    df['Apellido'] = df['Name'].str.split(', ', expand=True)[0]

    return df

def Decks(df):
    # The first letter of the Cabin values are the decks in which the cabins are located
    # Passengers labeled as M are the missing values in Cabin feature. 
    # I don't think it is possible to find those passengers' real Deck so I decided to use M like a deck
    df['Deck'] = df['Cabin'].apply(lambda s: s[0] if pd.notnull(s) else 'M')  

    df_trabajo=df[["Pclass","Family","Deck","Fare"]].copy()
    lista_fare_clase_familia_deck_mean=df_trabajo.groupby(by=["Pclass","Family","Deck"]).mean().rename(columns={'Fare': "Media"}).reset_index()

#   Con la informacion de este print se realizan los cambios de Deck siguientes
#    print(lista_fare_clase_familia_deck_mean)

# Passenger in the T deck is changed to A
    df["Deck"].replace(["T"], "A", inplace=True)

# Cambios de asignacion para los M por el tipo de Fare unitario / Pclass y Deck
    df.loc[(df.Deck == "M") & (df.Pclass == 1) & (df.Family == 2),"Deck"] = "D"
    df.loc[(df.Deck == "M") & (df.Pclass == 1) & (df.Family == 3) ,"Deck"] = "C"
    df.loc[(df.Deck == "M") & (df.Pclass == 2) & (df.Family == 1) ,"Deck"] = "D"
    df.loc[(df.Deck == "M") & (df.Pclass == 2) & (df.Family == 3) ,"Deck"] = "F"
    df.loc[(df.Deck == "M") & (df.Pclass == 2) & (df.Family == 4) ,"Deck"] = "F"
    df.loc[(df.Deck == "M") & (df.Pclass == 3) & (df.Family == 1) ,"Deck"] = "E"
    df.loc[(df.Deck == "M") & (df.Pclass == 3) & (df.Family == 2) ,"Deck"] = "E"
    df.loc[(df.Deck == "M") & (df.Pclass == 3) & (df.Family == 3) ,"Deck"] = "G"
    # Agrupamos en 3 grupos
    df['Deck'] = df['Deck'].replace(['A', 'B', 'C'], 'ABC') # A, B and C decks are labeled as ABC because all of them have only 1st class passengers
    df['Deck'] = df['Deck'].replace(['D', 'E'], 'DE') # D and E decks are labeled as DE because both of them have similar passenger class distribution and same survival rate
    df['Deck'] = df['Deck'].replace(['F', 'G'], 'FG') # F and G decks are labeled as FG because of the same reason above
    return df

def Median_ages(df):
    df['Age'] = df.groupby(["Sex", "Pclass"])["Age"].apply(lambda x: x.fillna(x.median()))
    return df

def Fare(df):
    df["Fare"] = df.groupby(["Parch", "SibSp", "Pclass"])["Fare"].apply(lambda x: x.fillna(x.median()))
    return df

def Cabin(df):
    df["Cabin"] = df.Cabin.fillna("U")
    df['Cabin'] = df['Cabin'].map(lambda c: c[0])
    return df

def Embarked(df):
    Embarked_mode=df["Embarked"].mode().value_counts().index[0]
    df["Embarked"] = df["Embarked"].fillna(Embarked_mode)
    return df

def Family(df):
    df['Family']=df['SibSp']+df['Parch']+1
    #El número 1 es tomando en cuenta al pasajero, símplemente estamos sumando el número de acompañantes con el pasajero

    #Podemos definir el tamaño de una familia de acuerdo al resultado del nuevo campo
    df['OneMemberFamily']=df['Family'].map(lambda s: 1 if s==1 else 0) 
    df['SmallFamily']=df['Family'].map(lambda s: 1 if s>= 2 and s<=4 else 0)
    df['BigFamily']=df['Family'].map(lambda s: 1 if s>4 else 0)
    return df

def Grupo_Family(df):
    df["Grupo_Familiar"]=""
    dups_series=df.pivot_table(index = ["Ticket"], aggfunc ="size", margins_name="Total")
    dups = pd.DataFrame(dups_series, columns=["Num_Personas"]).reset_index()
    
    # MISMO TICKET MISMO GRUPO FAMILIAR
    dups.Grupo_Familiar = np.where(dups.Num_Personas > 1, dups.Ticket, "NO_GRUPO")

    # SI NO TIENEN GRUPO FAMILIAR POR TICKET SI TIENEN MISMO APELLIDO Y MISMO NUMERO DE FAMILY o MISMO FARE EN LA MISMA CLASE SE CONSIDERAN MISMO GRUPO FAMILIAR
    df_Apellido_Family=df[["Apellido","Family","Grupo_Familiar","Pclass","Fare","Name"]].copy()
    lista_apellidos=df_Apellido_Family.groupby(by=["Apellido","Family","Grupo_Familiar","Pclass","Fare"]).count().rename(columns={'Name': "Num_Apellidos"}).reset_index()

    for i in range(len(df)):
        if df.Ticket[i] in dups.Grupo_Familiar:
            df.Grupo_Familiar[i] = df.Ticket[i]
        else:
            df.Grupo_Familiar[i] = "NO_GRUPO"
    
        if df.Grupo_Familiar[i] == "NO_GRUPO":
            if df.Apellido[i] in lista_apellidos.Apellido:
                if lista_apellidos[(lista_apellidos.Apellido==df.Apellido[i]) & (lista_apellidos.Family==df.Family[i]) &
                                    (lista_apellidos.Grupo_Familiar==df.Grupo_Familiar[i]) & (lista_apellidos.Pclass==df.Pclass[i]) &
                                    (lista_apellidos.Fare==df.Fare[i]) ].Num_Apellidos[i] > 1:

                    df.Grupo_Familiar[i] = df.Apellido[i]


def Estandarizar_Datos(df):
    
    listado_grupo = list(df.Grupo_Familiar.unique())
    listado_titulo = list(df.Title.unique())
    
    for i in range(len(df)):
        # PONEMOS VALORES NUMERICOS A GRUPO FAMILIAR
        if df.Grupo_Familiar[i] in listado_grupo:
            ind=listado_grupo.index(df.Grupo_Familiar[i])
            df.Grupo_Familiar[i]=int(ind)
    
            # PONEMOS VALORES NUMERICOS A TITULO
        if df.Title[i] in listado_titulo:
            ind_t=listado_titulo.index(df.Title[i])
            df.Title[i]=int(ind_t)

    df['Grupo_Familiar'] = df['Grupo_Familiar'].astype('int64')
    df['Title'] = df['Title'].astype('int64')

    return df

def Eliminar_Columnas(df):

    df = df.drop(["PassengerId","Name","Ticket","SibSp","Parch", "Cabin","Apellido"], axis=1, inplace=True)
        
    return df

def Escalar_Datos(df):

    df.Age = (df.Age - np.mean(df.Age, axis=0)) / (np.std(df.Age, axis=0))
    df.Fare = (df.Fare - np.mean(df.Fare, axis=0)) / (np.std(df.Fare, axis=0))
    df.Family = (df.Family - np.mean(df.Family, axis=0)) / (np.std(df.Family, axis=0))
    df.Grupo_Familiar = (df.Grupo_Familiar - np.mean(df.Grupo_Familiar, axis=0)) / (np.std(df.Grupo_Familiar, axis=0))
    df.Title = (df.Title - np.mean(df.Title, axis=0)) / (np.std(df.Title, axis=0))

    return df


def precision(tipo, y_test, y_pred):
    
    # Calculo de precisión del modelo
    from sklearn.metrics import precision_score
    precision = precision_score(y_test, y_pred, average='macro')
    print("MODELO: ",tipo)
    print("Precisión del modelo: ",precision)

    from sklearn.metrics import accuracy_score
    exactitud = accuracy_score(y_test, y_pred)
    print("Exactitud del modelo: ",exactitud)

    # Calcular la sensibilidad del modelo
    from sklearn.metrics import recall_score
    sensibilidad = recall_score(y_test, y_pred, average='macro')
    print("Sensibilidad del modelo: ",sensibilidad)

    #Calculo el puntaje F1 del modelo
    from sklearn.metrics import f1_score
    puntajef1 = f1_score(y_test, y_pred, average='macro')
    print("Puntaje F1 del modelo; ", puntajef1)
    
    puntaje_total = (precision+exactitud+sensibilidad+puntajef1)/4
    print("Puntaje Meedia del modelo; ", puntaje_total)
    print("\n \n")
    return

df_train = pd.read_csv("./data/train.csv") 
df_test = pd.read_csv("./data/test.csv") #sin columna de superviviente


# Para tratar la Engineering lo haremos con toda la base de datos completa
df_all = concat_df(df_train, df_test)

Name(df_all)
Fare(df_all)
Family(df_all)
Decks(df_all)
Grupo_Family(df_all)
Median_ages(df_all)
Cabin(df_all)
Embarked(df_all)
Eliminar_Columnas(df_all)
Estandarizar_Datos(df_all)
Escalar_Datos(df_all)


# GENERAMOS COLUMNAS DUMMIES
df_all = pd.get_dummies(df_all, columns=["Pclass","Sex","Embarked","Is_Married","OneMemberFamily","SmallFamily","BigFamily","Deck"], drop_first=True)


# Para la Prediccion volvemos a separar el Df en train y test
df_train, df_test = separar_df(df_all, df_train, df_test)

#Obtención de X, y
y = df_train["Survived"]
X = df_train.drop("Survived", axis=1)

# Entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Pruebo los posibles algoritmos a ensayar
# LogisticRegression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
acc_LG = accuracy_score(y_test, y_pred)

precision("LogisticRegression", y_test, y_pred)

# KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_KN = accuracy_score(y_test, y_pred)

precision("KNeighborsClassifier", y_test, y_pred)

# DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_DT = accuracy_score(y_test, y_pred)

precision("DecisionTreeClassifier", y_test, y_pred)

# RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_RF = accuracy_score(y_test, y_pred)

precision("RandomForestClassifier", y_test, y_pred)

# GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_NB = accuracy_score(y_test, y_pred)

precision("GaussianNB", y_test, y_pred)

#SVC
clf = SVC()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_SVC = accuracy_score(y_test, y_pred)

precision("SVC", y_test, y_pred)

#GradientBoostingClassifier
from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_GradientBC = accuracy_score(y_test, y_pred)

precision("GradientBoostingClassifier", y_test, y_pred)

# LightGBM - Light Gradient Boosting Machine
from lightgbm import LGBMClassifier
clf = LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_LightGBM = accuracy_score(y_test, y_pred)

precision("LightGBM - Light Gradient Boosting Machine", y_test, y_pred)

# EL QUE MEJOR RESULTADO ES EL LghtGBM
# LghtGBM - Light Gradient Boosting Machine
clf = LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc_LightGBM = accuracy_score(y_test, y_pred)


# Utilizo ese entrenamiento para el test.csv
y_pred = clf.predict(df_test)


# Genero el .csv a testar en platadorma
df_submision = pd.read_csv("./data/gender_submission.csv")

df_submision["Survived"] = y_pred.astype(int) 
df_submision.to_csv("./data/gender_submission_Final_Engineering.csv", index=False)
print("Documento generado")





