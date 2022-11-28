
import streamlit as st
import numpy as np
import pickle
import pandas as pd



st.set_page_config(page_icon="🚧", layout="wide")

def load_model():
    with open('Modelfinal.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

accuracy=data["Précision"]
modul=data["model"]

def explore():
    st.title("Information dur   Le modèle et leurs  erreurs")
    st.subheader('Grace a ce modèle on peut prédire la gravité d un accident par apport à 6 paramétres ')
    st.subheader(f" - Accuracy  :    {accuracy:.5f}  ")




def predicte():
    st.title("Prédire la gravité d'un accident dans  la route")
    st.write("Entrer les données:")
    
    input1 = st.selectbox("SPEEDING; (0 = No, 1 = Yes)", (0,1))
    input2= st.selectbox("INATTENTIONIND ; (0 = No, 1 = Yes)", (0,1))
    input3 = st.selectbox("UNDERINFL ; (0 = No, 1 = Yes)", (0,1))
    input4 = st.selectbox("ROAD CONDITION ;(0 = Dry, 1 = Mushy, 2 = Wet)", (0,1,2))
    input5 = st.selectbox("Weather Conditions ; (0 = Clear, 1 = Overcast and Cloudy, 2 = Windy, 3 = Rain and Snow", (0,1,2,3))
    input6= st.selectbox("LIGHTCND ; (0 = Light, 1 = Medium, 2 = Dark)", (0,1,2))
    
    
    submit = st.button("Predire la gravité")
    if submit:
        
        x1=np.array([[float(input1),float(input2),float(input3),float(input4),float(input5),float(input6)]])
        x1 = x1.astype(float)

        predire= modul.predict(x1)
        st.subheader(f"la prédiction de la ravité de l'accidente :    {predire[0]:.0f} ")
        st.text("0 : Gravité de matériel uniquement ")
        st.text("1 : Gravité humain et matériel")
    





st.sidebar.image('logo.jpeg', caption='ESI',channels="RGB")
st.text("")

switching=st.sidebar.radio("PRÉDIRE  OU EXPLORER DATA:", ("PRÉDIRE", "EXPLORER"))
st.text("")
if switching=="PRÉDIRE" :
    predicte()

else  :
    explore()

st.sidebar.header("Membre du projet:")
st.text("")
st.sidebar.text("-JAMERI Abdelkebir")
st.sidebar.text("-ETAIBI Salah Eddine")
st.sidebar.text("-El-Hassani Mohamed")
st.sidebar.text("-El-Jamaai Mohamed")
st.text("")
st.text("")

st.sidebar.header("Encardé par :")

st.sidebar.text(" Mme Najima DAOUDI")
