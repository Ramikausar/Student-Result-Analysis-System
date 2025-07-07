import pandas as pd

data = pd.read_excel("results.xlsx")
df = pd.DataFrame(data)

print("\n\n")
print(df.head().to_string(index=False))

# total mark
print("\n\n________________________________________ Total mark ___________________________________________\n")

df['total mark'] = (df['Hindi'] + df["English"]+ df["Science"]+ df["Maths"]+ df["History"]+ df["Geograpgy"])
print(df)

# percentage 
print("\n\n_____________________________________ Percentage ________________________________________\n")
Total_marks = 600
print('per/n')
df['Percentage'] = (df['total mark'] / Total_marks) * 100
df['Percentage'] = df['Percentage'].round(2)
print(df)

# adding pass and fail coloumn
subject_cols = ["Hindi", "English", "Science", "Maths", "History", "Geograpgy"]

df["Pass/Fail"] = df[subject_cols].lt(35).any(axis=1).map ({True: "Fail", False: "Pass"})
print("\n\n__________________________________________Pass/Fail____________________________________________\n")
print(df)