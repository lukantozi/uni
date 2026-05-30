import pandas as pd


pd.options.display.max_rows = 300


"""
============================================================
Part 1
============================================================
"""
# Task 1
df = pd.read_csv("students_dirty.csv")

# Task 2
print("Task 2:")
print(df.head(10), end='\n\n')

# Task 3
print("Task 3:")
r, c = df.shape
print(f"rows: {r}, columns: {c}", end='\n\n')

# Task 4
print("Task 4:")
print(df.dtypes, end='\n\n')

# Task 5
print("Task 5:")
print(df.describe(include = "number"), end='\n\n')

# Task 6
print("Task 6:")
print(df.count() - df.isna().sum())


"""
============================================================
Part 2
============================================================
"""
# Task 7
print()
print("Task 7:")
print(df["Name"], end='\n\n')

# Task 8
print("Task 8:")
new_df = df[["Name", "Grade"]]
print(new_df, end='\n\n')

# Task 9
print("Task 9:")
print(new_df.iloc[:5], end='\n\n')

# Task 10
print("Task 10:")
print(new_df.loc[df["City"] == "New York"], end='\n\n')

# Task 11
print("Task 11:")
print(new_df.loc[new_df["Grade"] > 85], end='\n\n')


# Task 12
print("Task 12:")
print(df.loc[(df["Passed"] == True) & (df["Age"] < 18)], end='\n\n')


"""
============================================================
Part 3
============================================================
"""
# Task 13
print("Task 13:")
print(df.isna().sum(), end='\n\n')

# Task 14
df.dropna(subset=["Name", "City"], inplace=True)

# Task 15
df.fillna({"Grade": df["Grade"].mean().round()}, inplace=True)
df.fillna({"Passed": True}, inplace=True)

# Task 16
df.drop_duplicates(inplace=True)

# Task 17
df.loc[(df["Grade"] > 100) | (df["Grade"] < 0), "Grade"] = df["Grade"].mean().round(2)

# Task 18
df["Exam_Date"] = pd.to_datetime(df["Exam_Date"])

# Task 19
print("Task 19:")
print(df["Name"].isna().sum() == 0, end='\n\n')
print(df["City"].isna().sum() == 0, end='\n\n')
print(df.loc[(df["Grade"] > 100) | (df["Grade"] < 0), "Grade"], end='\n\n')
print(df["Exam_Date"].dtypes == "datetime64[us]", end='\n\n')


"""
============================================================
Part 4
============================================================
"""
# Task 20
def grade_category(grade):
    if grade > 85:
        return "High"
    elif 70 <= grade <= 85:
        return "Medium"
    else:
        return "Low"

df["Grade_Category"] = df["Grade"].map(grade_category)

# Task 21
df["Grade"] = df["Grade"].round().astype(int)

# Task 22
df.sort_values("Grade", ascending=False, inplace=True)

# Task 23
df.reset_index(drop=True, inplace=True)

# Task 24
df["Age_in_2026"] = df["Age"] + 1


"""
============================================================
Part 5
============================================================
"""
# Task 25
print("Task 25:")
print(df.groupby("City")["Grade"].mean().round(), end='\n\n')

# Task 26
print("Task 26:")
print(df.groupby("Grade_Category")["Name"].count(), end='\n\n')

# Task 27
print("Task 27:")
print(df.groupby("City")["Grade"].max())
import pandas as pd


pd.options.display.max_rows = 300


"""
============================================================
Part 1
============================================================
"""
# Task 1
df = pd.read_csv("students_dirty.csv")

# Task 2
print("Task 2:")
print(df.head(10), end='\n\n')

# Task 3
print("Task 3:")
r, c = df.shape
print(f"rows: {r}, columns: {c}", end='\n\n')

# Task 4
print("Task 4:")
print(df.dtypes, end='\n\n')

# Task 5
print("Task 5:")
print(df.describe(include = "number"), end='\n\n')

# Task 6
print("Task 6:")
print(df.isna().sum())


"""
============================================================
Part 2
============================================================
"""
# Task 7
print()
print("Task 7:")
print(df["Name"], end='\n\n')

# Task 8
print("Task 8:")
new_df = df[["Name", "Grade"]]
print(new_df, end='\n\n')

# Task 9
print("Task 9:")
print(new_df.iloc[:5], end='\n\n')

# Task 10
print("Task 10:")
print(new_df.loc[df["City"] == "New York"], end='\n\n')

# Task 11
print("Task 11:")
print(new_df.loc[new_df["Grade"] > 85], end='\n\n')


# Task 12
print("Task 12:")
print(df.loc[(df["Passed"] == True) & (df["Age"] < 18)], end='\n\n')


"""
============================================================
Part 3
============================================================
"""
# Task 13
print("Task 13:")
print(df.isna().sum(), end='\n\n')

# Task 14
df.dropna(subset=["Name", "City"], inplace=True)

# Task 15
df.fillna({"Grade": df["Grade"].mean().round()}, inplace=True)
df.fillna({"Passed": True}, inplace=True)

# Task 16
df.drop_duplicates(inplace=True)

# Task 17
df.loc[(df["Grade"] > 100) | (df["Grade"] < 0), "Grade"] = df["Grade"].mean().round(2)

# Task 18
df["Exam_Date"] = pd.to_datetime(df["Exam_Date"])

# Task 19
print("Task 19:")
print(df["Name"].isna().sum() == 0, end='\n\n')
print(df["City"].isna().sum() == 0, end='\n\n')
print(df.loc[(df["Grade"] > 100) | (df["Grade"] < 0), "Grade"], end='\n\n')
print(df["Exam_Date"].dtypes == "datetime64[us]", end='\n\n')


"""
============================================================
Part 4
============================================================
"""
# Task 20
def grade_category(grade):
    if grade > 85:
        return "High"
    elif 70 <= grade <= 85:
        return "Medium"
    else:
        return "Low"

df["Grade_Category"] = df["Grade"].map(grade_category)

# Task 21
df["Grade"] = df["Grade"].round().astype(int)

# Task 22
df.sort_values("Grade", ascending=False, inplace=True)

# Task 23
df.reset_index(drop=True, inplace=True)

# Task 24
df["Age_in_2026"] = df["Age"] + 1


"""
============================================================
Part 5
============================================================
"""
# Task 25
print("Task 25:")
print(df.groupby("City")["Grade"].mean().round(), end='\n\n')

# Task 26
print("Task 26:")
print(df.groupby("Grade_Category")["Name"].count(), end='\n\n')

# Task 27
print("Task 27:")
print(df.groupby("City")["Grade"].max())
