import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))


st.title('Spam Text Classification')

message = st.text_input('Input Your Text/Message')

submit = st.button('Predict Now')

if submit:
    prediction = model.predict([message])
    
    if prediction[0] == 'spam':
        st.warning('Alert!!! Spam Detected!!!')
    else:
        st.success('No Spam Detected')