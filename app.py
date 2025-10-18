import streamlit as st

# Titre
st.title("Machine Décisionnelle - Sélecteur de Prompt")

# Description
st.write("Sélectionne un prompt dans le menu déroulant pour l'afficher.")

# Menu déroulant pour choisir le prompt
prompt_choice = st.selectbox(
    "Choisis le type de prompt :",
    ["V1 - Standard 🔵", "V2 - Avancé 🟡", "V3 - Extrême 🔴"]
)

# Contenu des prompts (texte intégral à coller ici)
prompts = {
    "V1 - Standard 🔵": """# Script GPT - Workflow opérationnel “micro micro-actions” extrême
Tu es un assistant expert en organisation de projets et en exécution opérationnelle. Ton rôle est de transformer **des notes brutes** en un **workflow ultra détaillé**, comprenant toutes les **micro-actions invisibles**, **micro-micro-actions**, **micro-micro-micro actions**, **micro-micro-micro-micro actions**, **Principe :**. chaque action est découpée en 3 à 5 micro-sous-actions, avec instructions ultra-détaillées, checklist, vérifications et plans B. Chaque étape doit être **une phrase complète et explicative**, incluant : quoi, qui, comment, pourquoi, conditions, dépendances et plans B. - Même les actions que quelqu’un pourrait juger “trop évidentes” doivent être écrites. - L’objectif est que **le flux opérationnel soit 100% externalisé** : aucune réflexion nécessaire, aucune étape oubliée, aucune zone grise. - Inclure **plans alternatifs / contournements** pour chaque risque ou blocage potentiel.
... (coller le reste du Prompt V1 ici) ...
""",
    "V2 - Avancé 🟡": """# Prompt for effective decision making (V2)
Transformer mes notes ou texte brut en un workflow opérationnel **ultra détaillé micro‑micro‑micro-actions**, prêt à exécuter, adapté à un environnement *extrêmement erratique et dispersé* : toutes les parties prenantes changent souvent d’avis, sont distraites et décident au dernier moment.
... (coller le reste du Prompt V2 ici) ...
""",
    "V3 - Extrême 🔴": """# Prompt V3 Hyper High Agency in Worst Erratic Settings
Transforme mes notes en un workflow opérationnel **ultra détaillé micro‑micro‑micro-actions**, prêt à exécuter, pour un environnement *pire du pire extrême* :
... (coller le reste du Prompt V3 ici) ...
"""
}

# Affichage du prompt sélectionné
st.subheader(f"Prompt sélectionné : {prompt_choice}")
st.code(prompts[prompt_choice], language='markdown')
