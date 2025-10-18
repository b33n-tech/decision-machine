import streamlit as st
import json

# Titre
st.title("Machine Décisionnelle - Sélecteur de Prompt")

# Charger les prompts depuis le fichier JSON
with open("prompts.json", "r", encoding="utf-8") as f:
    prompts_data = json.load(f)

# Menu déroulant
prompt_choice = st.selectbox(
    "Choisis le type de prompt :",
    list(prompts_data.keys())
)

# Afficher description
st.write(prompts_data[prompt_choice]["description"])

# Afficher le prompt complet
st.subheader("Prompt complet")
st.code(prompts_data[prompt_choice]["prompt"], language='markdown')
