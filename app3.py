import streamlit as st
import json

st.set_page_config(layout="wide")
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
selected_category = st.radio("Choisis une catégorie :", list(categories.keys()), horizontal=True)

# Champ de recherche
search_text = st.text_input("Rechercher un prompt :")

# Filtrer les prompts par catégorie et recherche
prompts_in_cat = {k: v for k, v in categories[selected_category].items() 
                  if search_text.lower() in k.lower() or search_text.lower() in v.get("description","").lower()}

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None

# Affichage des cartes en grille
cols_per_row = 3
cols = st.columns(cols_per_row)
for i, (key, value) in enumerate(prompts_in_cat.items()):
    col = cols[i % cols_per_row]
    with col:
        st.markdown(f"""
        <div style="
            border:1px solid #555; 
            padding:15px; 
            margin-bottom:10px; 
            border-radius:10px; 
            cursor:pointer; 
            background-color:#2a2a2a; 
            color:#eee;
        ">
        <b>{key}</b><br>
        <small>{value.get("description", "")}</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Select {key}", key=f"btn_{selected_category}_{i}"):
            st.session_state.selected_prompt = key

# Affichage du prompt sélectionné
if st.session_state.selected_prompt:
    prompt_key = st.session_state.selected_prompt
    prompt_info = prompts_data[prompt_key]

    st.markdown("---")
    st.header(f"Prompt sélectionné : {prompt_key}")
    st.write(prompt_info.get("description", "Pas de description disponible"))
    st.subheader("Prompt complet")
    st.text_area("Prompt", prompt_info.get("prompt", "Pas de prompt disponible"), height=400)
