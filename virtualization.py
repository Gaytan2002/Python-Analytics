import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("dta.csv") #copy/paste file name to insert full path

plt.figure(figsize=(10, 5))
plt.bar(df["Country"], df["Emissions"], color="blue")

plt.xlabel("Country")
plt.ylabel("Total Emissions")
plt.title("Total Emissions by Country (2021)")

plt.xticks(rotation=45)

plt.show()



