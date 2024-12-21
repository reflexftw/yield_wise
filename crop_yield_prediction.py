import pandas as pd

df = pd.read_csv("./Crop_Yield_Prediction.csv")

print(df.head())

crop_summary = pd.pivot_table(df, index="Crop", aggfunc="mean")
print(crop_summary)