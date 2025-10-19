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

# Variables pour gérer l'état du prompt sélectionné
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None

st.subheader("Choisis un prompt :")

# Créer des cartes cliquables avec des colonnes
cols = st.columns(3)  # 3 cartes par ligne, tu peux ajuster
for i, (key, value) in enumerate(prompts_data.items()):
    col = cols[i % 3]
    if col.button(key):
        st.session_state.selected_prompt = key

# Afficher le prompt sélectionné
if st.session_state.selected_prompt:
    selected_key = st.session_state.selected_prompt
    st.header(f"Prompt sélectionné : {selected_key}")

    description = prompts_data[selected_key].get("description", "Pas de description disponible")
    st.write(description)

    prompt_text = prompts_data[selected_key].get("prompt", "Pas de prompt disponible")
    st.subheader("Prompt complet")
    st.text_area("Prompt", prompt_text, height=400)
