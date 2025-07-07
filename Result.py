import pandas as pd

data = pd.read_excel("results.xlsx")
df = pd.DataFrame(data)

print("\n\n")
print(df.head().to_string(index=False))