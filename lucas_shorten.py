import pandas as pd

df = pd.read_csv("lucas_r.csv")
df = df.sample(frac=0.001)
df.to_csv("lucas.csv", index=False)