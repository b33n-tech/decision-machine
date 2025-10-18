import streamlit as st

st.set_page_config(page_title="Machine Décisionnelle", layout="wide")

st.title("🛠 Machine Décisionnelle - Générateur de Prompt")

# Choix du type de prompt
prompt_type = st.selectbox(
    "Choisis le type de prompt",
    ("V1 - Standard", "V2 - Avancé", "V3 - Extrême")
)

# Zone de texte pour le projet / notes brutes
user_input = st.text_area("Colle ton texte brut ici :", height=200)

# Définition des templates
prompt_templates = {
    "V1 - Standard": """
# Script GPT - Workflow opérationnel “micro micro-actions” extrême 
Tu es un assistant expert en organisation de projets et en exécution opérationnelle. Ton rôle est de transformer **des notes brutes** en un **workflow ultra détaillé**, comprenant toutes les **micro-actions invisibles**, **micro-micro-actions**, **micro-micro-micro actions**, **micro-micro-micro-micro actions**. 
Principe : chaque action est découpée en 3 à 5 micro-sous-actions, avec instructions ultra-détaillées, checklist, vérifications et plans B. Chaque étape doit être **une phrase complète et explicative**, incluant : quoi, qui, comment, pourquoi, conditions, dépendances et plans B. Même les actions “trop évidentes” doivent être écrites. 
Objectif : **flux opérationnel 100% externalisé**. 
---
Texte d'entrée : 
""",
    "V2 - Avancé": """
Transformer mes notes ou texte brut en un workflow opérationnel **ultra détaillé micro‑micro‑micro-actions**, prêt à exécuter, adapté à un environnement *extrêmement erratique et dispersé* : toutes les parties prenantes changent souvent d’avis, sont distraites et décident au dernier moment.
Le workflow doit :  
- Décomposer **chaque tâche en actions atomiques de 5‑15 minutes**.  
- Identifier **toutes les dépendances cachées et sous-dépendances** pour chaque action avant l’exécution.  
- Définir pour chaque action : Responsable, Deadline, Escalade.  
- Préparer **Path B** et **Path C**, notes séparées hors flux principal.  
- Fournir **messages prêts à envoyer** pour chaque contact.  
- Identifier **actions parallèles ou préparatoires**.  

Texte d'entrée :
""",
    "V3 - Extrême": """
Transforme mes notes en un workflow opérationnel **ultra détaillé micro‑micro‑micro-actions**, prêt à exécuter, pour un environnement *pire du pire extrême* :  
- Tout est bloqué, erratique et dispersé à tous les niveaux.  
- Aucune partie prenante ne prend de responsabilité, ne répond, ni ne valide quoi que ce soit.  
- Toutes décisions implicites et dépendances cachées doivent être **déjà transformées en actions concrètes et précises**, directement exécutables.  
- Chaque tâche doit inclure : Responsable (moi par défaut), Deadline, Escalade immédiate.  
- Préparer Path B, C, D, E avec instructions précises et messages prêts.  
- Inclure pré-autorisations, shadow booking et split orders si nécessaire.  
- Flux principal : lisible, directement exécutable, activation automatique des Paths alternatifs dès dépassement de délai.  

Texte d'entrée :
"""
}

# Génération du prompt final
if user_input.strip() != "":
    final_prompt = prompt_templates[prompt_type] + user_input
    st.subheader("Prompt généré :")
    st.code(final_prompt, language="markdown")
else:
    st.info("Colle ton texte brut pour générer le prompt.")
