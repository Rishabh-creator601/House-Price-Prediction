import streamlit as st 



st.title("Make Some Predictions")

bedrooms =  float(st.slider("Choose No OF Bedrooms",0,9,1))
bathrooms =  float(st.slider("Choose No of Bathrooms",0,8,1))
sqft_living  = st.number_input( "Insert The area of Living Room (in square feet)",value=None, placeholder="min : 400 max: 13000",min_value=370,max_value=13540)
sqft_basement  = st.number_input( "Insert The area of Basement  (in square feet)",value=None, placeholder="min : 0 max: 4800",min_value=0,max_value=4800)
floors = float(st.slider("Enter No of Floors",1,4,1))
waterfront_ = st.checkbox("Have any WaterFront in house ?")
waterfront = 1 if waterfront_ == True else 0
view = st.slider("How much do you want to rate the view ?",0,4,1)
condition = st.slider("How much do you want to rate the condition of the house ?",0,5,1)




values = [bedrooms,bathrooms,sqft_living,floors,waterfront,view,condition,sqft_basement]

model = st.session_state["model"]

if st.button("Predict"):
    value  = model.predict([values])[0]
    st.info(f"The price of the house will be : ${value}")