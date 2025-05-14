
import streamlit as st
import pandas as pd
#Load the csv file
df=pd.read_csv("cultural_art_forms.csv")
#AppTitle
st.title("Explored Indian Traditional Art_Forms)
selected_state=st.selectbox("Select a state",df["State"].unique())
filtered=df[df["State]== selected_state]
st.write("**Traditional Art Forms**",filtered["Art_Forms"].values(0))
