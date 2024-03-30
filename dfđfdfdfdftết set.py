
   #Pandas Series
#Tạo một Pandas Series từ numpy.array.
#Tạo một Pandas Series từ mảng không có index.
#Tạo một Pandas Series từ mảng có index.
import pandas as pd
import numpy as np

arr = np.array([20,30,40,50,60])
series_from_array = pd.Series(arr)
print ("Pandas series from numpy.array:")
print(series_from_array)
# create pandas series from array without index
arr_no_index = [20,30,40,50,60]
series_no_index = pd.Series(arr_no_index)
print("\nPandas Series from arr without index:")
print(series_no_index)
# Create Pandas series from array without index
arr_with_index = np.array([20,30,40,50,60])
index = ['a','b','c','d','e']
series_with_index = pd.Series(arr_with_index, index=index)
print("\nPandas Series from array have index: ")
print(series_with_index)