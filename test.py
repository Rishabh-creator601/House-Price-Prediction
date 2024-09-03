import pandas as pd
from ydata_profiling import ProfileReport
cols  = ["date","sqft_lot","street","city","statezip","country","yr_built","yr_renovated"]

data = pd.read_csv("data.csv")

# profile = ProfileReport(data,title="HOUSE PRICE PREDICTION REPORT")


# profile.to_file("full_report.html")

# data = data.drop(columns=cols,index=1)

# profile = ProfileReport(data,title="HOUSE PRICE PREDICTION REPORT")

# profile.to_file("edited_report.html")



# print("Done")

for i in data.columns:
    print("- " + i.capitalize())