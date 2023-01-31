import pandas as pd
import numpy as np

df = pd.read_csv('datatsets/dailyActivity_merged.csv')

to_drop = ['LoggedActivitiesDistance']

df.drop(to_drop, inplace=True, axis=1)

print(df)