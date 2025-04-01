#'streamlit' è libreria di python che serve per creare applicazioni, in R si usa shiny.
# Flusk e jungle sono genitori di stream lit. 
# Jungle è molto forte, ma molto complicato. Flusk è evoluzione di jungle, che permetteva di fare stessa cosa ma più semplice, ma aveva bisogno di htmlcss.
# Streamlit invece ha bisogno di htmlcss, anche se si può usare per migliorarlo. 

# Noi usiamo streamlit per creare una interfaccia il più semplice possibile, tipo uno sbarra in cui scrivere e basta :)

import os
import sys
sys.path.append(os.path.abspath('..'))
from src import config
import streamlit as st
import streamlit_extras 
from streamlit_extras.let_it_rain import rain
import pickle

# Load the model and vectorizer
#with open(f"{config.MODELS_PATH}random_forest.pickle", "rb") as file:
#    model = pickle.load(file)

with open(f"{config.MODELS_PATH}vectorizer.pickle", "rb") as f:
    vectorizer = pickle.load(f)

st.title("Tect Classification")

# Text input
user_input = st.text_area("Enter text to classify", "")

# Text to choice the model
scelta = st.selectbox('Scegli un\'opzione:', ['Random Forest', 'Logistic Regression'])

if scelta == 'Random Forest':
    with open(f"{config.MODELS_PATH}random_forest.pickle", "rb") as file:
        model = pickle.load(file)
else: #scelta == 'Logistic Regression':
    with open(f"{config.MODELS_PATH}logistic.pickle", "rb") as file:
        model = pickle.load(file)


# Predict when button is clicked
if st.button("Classify"):
    if user_input.strip() == "" :
        st.warning("Please enter some text.")
    else:
        # Transform input and predict
        X = vectorizer.transform([user_input])
        prediction = model.predict(X)[0]
        if prediction == 'positive' :
            st.success(f"Predicted class: {prediction}")
            st.balloons()
        elif prediction == 'negative': 
            st.warning(f"Predicted class: {prediction}")
            rain(emoji='🚩', falling_speed= 3)
        else:
            st.warning(f"Predicted class: {prediction}")
