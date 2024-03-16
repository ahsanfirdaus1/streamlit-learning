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

    #taxi_data = pd.read_csv('dataset\\taxi\\taxi_fare\\train.csv')
    taxi_data = pd.read_csv('dataset/taxi/taxi_fare/train.csv')
    st.write(taxi_data.head(20))

    st.subheader('Passengers Amount Distribution')
    passenger_amount = pd.DataFrame(taxi_data['num_of_passengers'].value_counts()).head(50)
    st.bar_chart(passenger_amount)


with features:
    st.header('The features I created')

    st.markdown('* **first feature:** I created this feature because of this.. I calculated this logic..')
    st.markdown('* **second feature:** I created this feature because of this.. I calculated this logic..')
    


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')




