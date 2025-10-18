import streamlit as st

# Titre de l'application
st.title("Machine Décisionnelle - Sélecteur de Prompt")

# Description
st.markdown("""
Choisis le type de prompt que tu souhaites afficher.  
L'application te montrera uniquement le prompt sélectionné, prêt à être copié-collé.
""")

# Tableau récapitulatif des types de prompt
prompt_info = {
    "V1 - Standard 🔵": {
        "Niveau": "Standard",
        "Cible": "Projets normaux, débutants",
        "Philosophie": "Tout expliciter, même l’évident"
    },
    "V2 - Avancé 🟡": {
        "Niveau": "Avancé",
        "Cible": "Environnements erratiques",
        "Philosophie": "Anticiper l’imprévisible"
    },
    "V3 - Extrême 🔴": {
        "Niveau": "Extrême",
        "Cible": "Milieux toxiques/bloquants",
        "Philosophie": "Radical High Agency"
    }
}

# Affichage du tableau récap
st.subheader("Types de Prompt")
for key, value in prompt_info.items():
    st.write(f"**{key}**")
    st.write(f"- Niveau : {value['Niveau']}")
    st.write(f"- Cible : {value['Cible']}")
    st.write(f"- Philosophie : {value['Philosophie']}")
    st.write("---")

# Sélecteur de prompt
prompt_choice = st.selectbox(
    "Sélectionne le prompt à afficher :",
    ["V1 - Standard 🔵", "V2 - Avancé 🟡", "V3 - Extrême 🔴"]
)

# Contenu des prompts (textes bruts)
prompts = {
    "V1 - Standard 🔵": """# Script GPT - Workflow opérationnel “micro micro-actions” extrême
Tu es un assistant expert en organisation de projets et en exécution opérationnelle...
(ici coller tout le texte intégral du Prompt V1)
""",
    "V2 - Avancé 🟡": """# Prompt for effective decision making (V2)
Transformer mes notes ou texte brut en un workflow opérationnel ultra détaillé...
(ici coller tout le texte intégral du Prompt V2)
""",
    "V3 - Extrême 🔴": """# Prompt V3 Hyper High Agency in Worst Erratic Settings
Transforme mes notes en un workflow opérationnel ultra détaillé...
(ici coller tout le texte intégral du Prompt V3)
"""
}

# Affichage du prompt sélectionné
st.subheader(f"Prompt sélectionné : {prompt_choice}")
st.code(prompts[prompt_choice], language='markdown')
