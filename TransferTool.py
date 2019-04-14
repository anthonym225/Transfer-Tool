import pandas as pd
CollegeList = pd.read_csv("ForbesTopColleges.csv")
ColList = pd.DataFrame(CollegeList)

print(ColList)
