
import pandas as pd

data = pd.read_csv("operations_cleaned.csv", parse_dates=[1,2],sep= ',',
    decimal= '.', dayfirst=True )

inline()