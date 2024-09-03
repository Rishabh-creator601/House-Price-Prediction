import streamlit as st 
import pandas as pd
from pathlib import Path



cols  = ["date","sqft_lot","street","city","statezip","country","yr_built","yr_renovated"]


def load_data(cols,full=True):
    data = pd.read_csv("./data.csv")
    if full == False :
        data = data.drop(columns=cols,axis=1)
    return data
 
 
 
st.title("<  DATA  >")
 
 

    
report = "partial"
 
 
if st.checkbox("Show Full Dataset(columns not included in Training)",False):
    data = load_data(cols)
    report = "full"

else:
    data = load_data(cols,full=False)
    report = "partial"






st.dataframe(data,use_container_width=True)


st.html(" <h1> DOWLOAD EDA  REPORT </h1> ")






if report  == "partial":
    with open("records/edited_report.html","rb") as f:
        st.download_button("EDA REPORT",f,"report.html")




if report  == "full":
    with open("records/full_report.html","rb") as f:
        st.download_button("FULL EDA REPORT",f,"report.html")

    

    
    





