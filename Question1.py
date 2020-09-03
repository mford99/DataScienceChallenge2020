import pandas as pd
import numpy as np
import matplotlib

#Read-in the data as a pandas dataframe
DataScienceCSV = pd.read_csv("DataScience.csv")

print(DataScienceCSV["order_amount"].describe())

print("\nThe median is: " + str(DataScienceCSV["order_amount"].median()))

print(DataScienceCSV["order_amount"].quantile(q=0.9))

q1 = DataScienceCSV["order_amount"].quantile(q=0.25)
q2 = DataScienceCSV["order_amount"].quantile(q=0.5)
q3 = DataScienceCSV["order_amount"].quantile(q=0.75)
IQR = q3 - q1

FilteredData = DataScienceCSV[(DataScienceCSV["order_amount"] < q2 + IQR * 2) & (DataScienceCSV["order_amount"] > q2 - IQR * 2)]
print("The filered data is:\n")
print(FilteredData["order_amount"].describe())

print(FilteredData["order_amount"].median())
