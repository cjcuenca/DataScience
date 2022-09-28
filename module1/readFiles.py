"""
    Realización de la lectura de distintos archivos
"""
import pandas as pd
import settings

# Leer arcivos con pandas:

# CSV
csvFile = settings.MEDIA_ROOT + "/Iris.csv"

df = pd.read_csv(csvFile)

print("CSV file: ", df)

# convertir a xlsx:
# Instalar pip install xlwt openpyxl xlsxwriter xlrd

# df.to_excel(settings.MEDIA_ROOT  + '/dataIris.xlsx')
# df.to_csv(settings.MEDIA_ROOT + "/dataIris.csv")

# Excel .xlsx

# excelFile = settings.MEDIA_ROOT + "/dataIris.xlsx"

# df_xlsx = pd.read_excel(excelFile)

# print("Excel file: ", df_xlsx)

# convertir a json
# df.to_json(settings.MEDIA_ROOT  + '/dataIris.json')

# Json .json
# jsonFile = settings.MEDIA_ROOT + "/dataIris.json"

# df_json = pd.read_json(jsonFile)

# print("Json file: ", df_json)

# convertir a html
# df.to_html(settings.MEDIA_ROOT  + '/dataIris.html')

# HTML .html
# Instalar pip install lxml
# htmlFile = settings.MEDIA_ROOT + "/dataIris.html"

# df_html = pd.read_html(htmlFile)

# print("Html file: ", df_html)


# # Otra forma es con with open:

# CSV
# df_csv2 = pd.DataFrame(columns=['SepalLengthCm', 'SepalWidthCm',
#                                 'PetalLengthCm', 'PetalWidthCm',
#                                 'Species'])

# with open(csvFile, "r") as csv:
#     # print(csv.read())
#     # print(csv.readlines())
#     list_SepalLength = []
#     list_SepalWidth = []
#     list_PetalLength = []
#     list_PetalWidth = []
#     list_Species = []

#     for line in csv:
#         line = line.replace("\n", "")
#         list_row = line.split(",")

#         list_SepalLength.append(list_row[1])
#         list_SepalWidth.append(list_row[2])
#         list_PetalLength.append(list_row[3])
#         list_PetalWidth.append(list_row[4])
#         list_Species.append(list_row[5])

#     df_csv2['SepalLengthCm'] = list_SepalLength
#     df_csv2['SepalWidthCm'] = list_SepalWidth
#     df_csv2['PetalLengthCm'] = list_PetalLength
#     df_csv2['PetalWidthCm'] = list_PetalWidth
#     df_csv2['Species'] = list_Species

# df_csv2 = df_csv2.iloc[1:]
# print(df_csv2)


# ejemplo TXT de manipulación del archivo

# Lectura del archivo

# f = open(settings.MEDIA_ROOT + "/test.txt", "r")
# print(f.read())
# f.close()

# f = open(settings.MEDIA_ROOT + "/test.txt", "a")
# print(f.write("\nInsertando Línea"))
# f.close()