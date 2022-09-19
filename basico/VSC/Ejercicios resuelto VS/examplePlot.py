# pip install plotly-express
import plotly.express as px
import matplotlib.pyplot as plt

df = px.data.iris()  # iris (pandas DataFrame)

print(df)

versicolor = df[df["species_id"] == 2]

# print(versicolor)

figure = versicolor.plot(kind="bar")
plt.show()