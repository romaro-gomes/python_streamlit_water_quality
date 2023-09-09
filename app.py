import streamlit as st
import pandas as pd
import pickle
from PIL import Image

image_bad=Image.open('cat_dont_drink.jpeg')
image_good = Image.open('cat_drink.jpeg')
st.title('Help! That water is safe for my pet?😟',)

st.sidebar.header('Select Water Parameters')    

st.subheader('User Inpute Parameters')

def user_input_features():
    ph = st.sidebar.slider('ph', 0.2,15.0, 7.0)
    Hardness= st.sidebar.slider('Hardness', 73.0,318.0, 195.0)
    Solids= st.sidebar.slider('Solids', 320.0,57000.0, 20000.0)
    Chloramines= st.sidebar.slider('Chloramines',1.2 ,14.0, 7.0)
    Sulfate= st.sidebar.slider('Sulfate', 129.0,482.0, 333.0)
    Conductivity= st.sidebar.slider('Conductivity', 80.0,754.0, 426.0)
    Organic_carbon= st.sidebar.slider('Organic carbon', 2.2,28.0, 14.0)
    Trihalomethanes= st.sidebar.slider('Trihalomethanes', 8.5,124.0, 66.0)
    Turbidity= st.sidebar.slider('Turbidity', 1.4,6.5, 4.0)
    data= {
            'ph':ph, 
            'Hardness':Hardness,
            'Solids':Solids,
            'Chloramines':Chloramines,
            'Sulfate':Sulfate,
            'Conductivity':Conductivity,
            'Organic_carbon':Organic_carbon,
            'Trihalomethanes':Trihalomethanes,
            'Turbidity':Turbidity}
        
    features = pd.DataFrame(data,index=[0])
    return features

df=user_input_features()
st.write(df)


if st.button('Predict'):
    pipeline = pickle.load(open('pipeline.pkl','rb'))
    model=pickle.load(open('model.pkl','rb'))

    X=pipeline.transform(df)
    predict=model.predict(X)


    if predict == 0:
        st.title("That water is safe for your pet")
        st.image(image_good)
    else:
        st.title('Dont give that for your pet! You will kill it')
        st.image(image_bad)

st.caption('Dataset source: https://www.kaggle.com/datasets/adityakadiwal/water-potability')