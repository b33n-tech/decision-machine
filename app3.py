import streamlit as st
import json

# Titre de l'application
st.title("Machine Décisionnelle - Sélecteur de Prompt")

# Charger le JSON
try:
    with open("prompts.json", "r", encoding="utf-8") as f:
        prompts_data = json.load(f)
except Exception as e:
    st.error(f"Erreur lors du chargement du JSON : {e}")
    st.stop()

# Organiser les prompts par catégorie
categories = {}
for key, value in prompts_data.items():
    cat = value.get("categorie", "Sans catégorie")
    if cat not in categories:
        categories[cat] = {}
    categories[cat][key] = value

# Onglets par catégorie
selected_category = st.radio("Choisis une catégorie :", list(categories.keys()))

# Sélection dans la catégorie
st.subheader(f"Prompts dans la catégorie : {selected_category}")

prompts_in_cat = categories[selected_category]
cols = st.columns(3)  # 3 cartes par ligne

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None

# Affichage des cartes cliquables
for i, (key, value) in enumerate(prompts_in_cat.items()):
    col = cols[i % 3]
    with col:
        if st.button(key, key=f"btn_{selected_category}_{i}"):
            st.session_state.selected_prompt = key
        st.caption(value.get("description", ""))

# Affichage du prompt sélectionné
if st.session_state.selected_prompt:
    prompt_key = st.session_state.selected_prompt
    prompt_info = prompts_data[prompt_key]

    st.header(f"Prompt sélectionné : {prompt_key}")
    st.write(prompt_info.get("description", "Pas de description disponible"))
    st.subheader("Prompt complet")
    st.text_area("Prompt", prompt_info.get("prompt", "Pas de prompt disponible"), height=400)
