
import streamlit as st
from get_and_predict import price_prediction

st.set_page_config(layout="wide")

st.markdown(body="<h1 style='text-align: center'>CALCULATE THE PRICE OF YOUR DIAMOND</h1>", unsafe_allow_html=True)
st.title('')

col1, col3, col2 = st.columns([1, 0.2, 1])

with col1:
    weight = st.number_input(label="Weight of the diamond (0.2g -- 5.01g):")
    st.subheader('')

    cut = st.selectbox(label="Select diamond cut quality:", options=["Select the diamond cut quality", "Fair", 
                                                                    "Good", "Very Good", "Premium", "Ideal"])

    if cut == "Select the diamond cut quality":
        st.warning("🚨 Select one of the diamond cut quality 🚨")

    st.subheader('')
    
    
with col2:
    length = st.number_input(label="Length of the diamond (0mm -- 10.74gmm):")
    st.subheader("")
    
    width = st.number_input(label="Width of the diamond (0mm -- 58.9mm):")
    st.subheader("")

    
colum1, colum2, colum3 = st.columns([1, 0.2, 1])

with colum1:
    color = st.selectbox(label="Select diamond color quality:", options=["Select the diamond color quality", "D (Best)", 
                                                                        "E", "F", "G", "H", "I", "J (Worst)"])

    if color == "Select the diamond color quality":
        st.warning("🚨 Select one of the diamond color quality 🚨")
    
    st.subheader('')

with colum3:
    depth = st.number_input(label="Depth of the diamond (0mm -- 31.8mm):")
    st.subheader("")
    
    
column1, column2, column3 = st.columns([1, 0.2, 1])

with column1:
    clarity = st.selectbox(label="Select diamond clarity quality:", options=["Select the diamond clarity quality", "I1 (worst)", 
                                                                             "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF (best)"])
    
    if clarity == "Select the diamond clarity quality":
        st.warning("🚨 Select one of the diamond clarity quality 🚨")
        
    st.subheader("")

with column3:
    table = st.number_input(label="Select the width of top of diamond relative to widest point (43mm -- 95mm):")
    result = st.button(label="GET THE PRICE OF THE DIAMOND")
    

if result:
    price = price_prediction(weight, cut, length, width, color, depth, clarity, table)
    
    st.title(f"The price of your diamond is {price}€")