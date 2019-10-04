# Source: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

import numpy as np
import pandas as pd


# MARK: 1
series1 = pd.Series([1, 3, 5, np.nan, 7])


# MARK: 2. Tabular data (data frames)
# Data frames represent tabular data.
dates = pd.date_range("20191003", periods=6)
dataFrame1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["Column 1", "Column 2", "Column 3", "Column 4"])

dataFrame2 = pd.DataFrame({
    "Date": pd.Timestamp("20191001"),
    "Value 1": pd.Series([1, 2, 3, 4]),
    "Value 2": np.arange(4),
    "Value 3": pd.Categorical(["test", "train", "test", "train"]),
    "Constant": "a constant"
})
print(dataFrame2)

dataFrame2Types = dataFrame2.dtypes    # datetime64[ns], int64, int64, category, object

# Print a column.
# print(dataFrame2.Date, "\n")

# Top and bottom rows.
# top2Rows = dataFrame2.head(2)
# bottom2Rows = dataFrame2.tail(2)

# ???
# print(dataFrame2.index, "\n")
# print(dataFrame2.columns, "\n")

# To numpy
# NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column.
# When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame.
# DataFrame.to_numpy() does not include the index or column labels in the output.
# numpyRepresentation2 = dataFrame2.to_numpy()
# print(numpyRepresentation2)
# print(numpyRepresentation2.dtype)    # All cells are casted to `object`.

# Calculate max, min, mean, ... of columns.
# print(dataFrame2.describe())

# Transpose (even the labels are also transposed).
# print(dataFrame2.T)

# Sorting by column label???
# print(dataFrame2.sort_index(axis=1, ascending=True))

# Sorting by a value. VERY USEFUL 😄😄😄!!!
print(dataFrame2.sort_values(by="Value 1", ascending=False))

print("Quitting pandas test...")
