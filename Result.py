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

# csv file for failed and pass student 
fail_student = df[df["Pass/Fail"] == "Fail"]
pass_student = df[df["Pass/Fail"] == "Pass"]

fail_student.to_csv("Fail student.csv",index=False)
pass_student.to_csv("pass student.csv",index=False)

# garde 90 A++, 80 A+, 75 A, 65 to 74 B++, 55 to 64 B+, 50 to 54 B, 40 to 50 C , 30 to 40 D
df.loc[df["Pass/Fail"] == "Fail", "Grade"] = "F"

# Now assign grades only to students who passed
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 90), "Grade"] = "A++"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 80) & (df["Percentage"] < 90), "Grade"] = "A+"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 75) & (df["Percentage"] < 80), "Grade"] = "A"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 65) & (df["Percentage"] < 75), "Grade"] = "B++"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 55) & (df["Percentage"] < 65), "Grade"] = "B+"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 50) & (df["Percentage"] < 55), "Grade"] = "B"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 40) & (df["Percentage"] < 50), "Grade"] = "C"
df.loc[(df["Pass/Fail"] == "Pass") & (df["Percentage"] >= 30) & (df["Percentage"] < 40), "Grade"] = "D"
print("\n\n_____________________________________________GRADE_______________________________________________\n")
print(df)

