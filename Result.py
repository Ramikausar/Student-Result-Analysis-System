import pandas as pd

data = pd.read_excel("results.xlsx")
df = pd.DataFrame(data)

print("\n\n")
print(df.head().to_string(index=False))

# total mark
print("\n\n________________________________________ Total mark ___________________________________________\n")

df['total mark'] = (df['Hindi'] + df["English"]+ df["Science"]+ df["Maths"]+ df["History"]+ df["Geograpgy"])
print(df.to_string(index=False))

# percentage 
print("\n\n_____________________________________ Percentage ________________________________________\n")
Total_marks = 600

df['Percentage'] = (df['total mark'] / Total_marks) * 100
df['Percentage'] = df['Percentage'].round(2)
print(df.to_string(index=False))

# adding pass and fail coloumn
subject_cols = ["Hindi", "English", "Science", "Maths", "History", "Geograpgy"]

df["Pass/Fail"] = df[subject_cols].lt(35).any(axis=1).map ({True: "Fail", False: "Pass"})
print("\n\n__________________________________________Pass/Fail____________________________________________\n")
print(df.to_string(index=False))

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
print(df.to_string(index=False))

# Average score in all subject
print("\n\n___________________ Average subject score________________\n")

subject_cols = ["Hindi", "English", "Science", "Maths", "History", "Geograpgy"]
print(df[subject_cols].mean()) # get average mark of subjects 


# Average marks of student
print("\n\n___________________________ Average marks of student ______________________________________\n\n")

subject_cols = ['Hindi', 'English', 'Science', 'Maths', 'History', 'Geograpgy'] 
df["Average Marks"] = df[subject_cols].mean(axis=1).round(2)   # axis=1 use for row 
print(df.to_string(index=False))

print("\n\n___________________________highest score______________________________________\n\n")
subject_cols = ["Hindi", "English", "Science", "Maths", "History", "Geograpgy"]
 
top_scores = []
for subject in df.columns[1:7]:                                 # subject name is geting stored 
    max_score = df[subject].max()                               # max subject stored
    top_students = df[df[subject] == max_score]                 # seprating score where subject have high score as max_score
    for _, row in top_students.iterrows():                      # interrows go through all rows
            top_scores.append({                                 # Adds a dictionary to the top_scores 
                "roll number" : row["roll number"],
                "subject" : subject,
                "score" : max_score
            })
top_scores_df = pd.DataFrame(top_scores,)
print(top_scores_df.to_string(index=False))

print("\n\n___________________________ lowest score______________________________________\n\n")
min_scores = []
for subject in df.columns[1:7]:                                 # subject name is geting stored 
    min_score = df[subject].min()                               # min score subject stored
    min_students = df[df[subject] == min_score]                 # seprating score where subject have lowest score as max_score
    for _, row in min_students.iterrows():                      # interrows go through all 
            min_scores.append({
                "roll number" : row["roll number"],
                "subject" : subject,
                "score" : min_score
            })
            
min_scores_df = pd.DataFrame(min_scores)
print(min_scores_df.to_string(index=False))

