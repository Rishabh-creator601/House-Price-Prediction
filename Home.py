import streamlit as st 
import pickle
import pandas as pd

@st.cache_resource
def load_model():
    
    model = pickle.load(open("model.pkl","rb"))
    return model 
 

model =  load_model()



if "model" not in st.session_state:
    st.session_state["model"] = model 
    

st.sidebar.success("Select Any Page From here")






st.header("About Dataset")
st.markdown("the datset is Downloadable from [Kaggle dataset](https://www.kaggle.com/datasets/shree1992/housedata) ")
st.markdown(""" The dataset contains the following Columns :
- ~~Date~~
- Price
- Bedrooms
- Bathrooms
- Sqft_living
- ~~Sqft_lot~~
- Floors
- Waterfront
- View
- Condition
- Sqft_above
- Sqft_basement
- ~~Yr_built~~
- ~~Yr_renovated~~
- ~~Street~~
- ~~City~~
- ~~Statezip~~
- ~~Country~~  
 **Note :The Columns that are strikethrough are not in trained model**""")




st.header("About Model")

st.markdown(""" **Model** : **RandomForestRegressor** \n
**Accuracy : 87%** \n
You can further make predictions on : [prediction](https://housepredprice.streamlit.app/Prediction) \n
And explore about data on : [data](https://housepredprice.streamlit.app/data)  """)








