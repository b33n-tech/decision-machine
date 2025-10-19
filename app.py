import streamlit as st
import json

# Titre de l'application
st.title("Machine Décisionnelle - Sélecteur de Prompt")

# Charger les prompts depuis le fichier JSON
try:
    with open("prompts.json", "r", encoding="utf-8") as f:
        prompts_data = json.load(f)
except FileNotFoundError:
    st.error("Le fichier 'prompts.json' est introuvable. Vérifiez le chemin.")
    st.stop()
except json.JSONDecodeError as e:
    st.error(f"Erreur lors du parsing JSON : {e}")
    st.stop()
except Exception as e:
    st.error(f"Erreur inattendue : {e}")
    st.stop()

# Menu déroulant pour choisir le prompt
prompt_choice = st.selectbox(
    "Choisis le type de prompt :",
    list(prompts_data.keys())
)

# Afficher titre dynamique
st.header(f"Prompt sélectionné : {prompt_choice}")

# Afficher la description
description = prompts_data[prompt_choice].get("description", "Pas de description disponible")
st.write(description)

# Afficher le prompt complet avec scroll
prompt_text = prompts_data[prompt_choice].get("prompt", "Pas de prompt disponible")
st.subheader("Prompt complet")
st.text_area("Prompt", prompt_text, height=400)
