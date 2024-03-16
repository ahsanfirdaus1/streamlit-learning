import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome to my awsome data science project!')
    st.text('In this project I look into the transactions of taxis in NYC. ...')

with dataset:
    st.header('NYC taxi dataset')
    st.text('I found this dataset on kaggle.com')

    taxi_data = pd.read_csv('dataset\\taxi\\taxi_fare\\train.csv')
    st.write(taxi_data.head(20))


with features:
    st.header('The features I created')
    


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')




