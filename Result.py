import pandas as pd

data = pd.read_excel("results.xlsx")
df = pd.DataFrame(data)

print("\n\n")
print(df.head().to_string(index=False))

# total mark
print("\n\n________________________________________ Total mark ___________________________________________\n")

df['total mark'] = (df['Hindi'] + df["English"]+ df["Science"]+ df["Maths"]+ df["History"]+ df["Geograpgy"])
print(df)
