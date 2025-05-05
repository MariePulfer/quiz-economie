import streamlit as st
import random

st.set_page_config(page_title="Quiz Économie", page_icon="📚")
st.title("📚 Révision - Économie : Les modes de vente")

# -------------------------------
# Données du quiz (extrait de ton cours)
# -------------------------------
questions = [
    {
        "question": "Quel type de vente permet de comparer rapidement les produits ?",
        "options": ["Vente au comptant", "Vente aux enchères", "Vente par internet"],
        "answer": "Vente par internet",
        "explanation": "La vente par internet permet de comparer facilement les prix de plusieurs produits."
    },
    {
        "question": "Dans une vente à crédit, que signifie une échéance ?",
        "options": ["Un rabais appliqué au prix", "La date de fin de garantie", "La date limite pour un paiement"],
        "answer": "La date limite pour un paiement",
        "explanation": "Une échéance est une date à laquelle un paiement doit être effectué, souvent mensuel."
    },
    {
        "question": "Qui est propriétaire du bien dans un contrat de leasing ?",
        "options": ["L'utilisateur", "La société de leasing", "Le vendeur d'origine"],
        "answer": "La société de leasing",
        "explanation": "Le bien est acquis par la société de leasing, qui reste propriétaire pendant toute la durée du contrat."
    },
    # Tu peux ajouter plus de questions ici...
]

# -------------------------------
# Initialisation de session
# -------------------------------
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False
if "selected" not in st.session_state:
    st.session_state.selected = None

# -------------------------------
# Logique principale
# -------------------------------
if st.session_state.index < len(questions):
    q = questions[st.session_state.index]
    st.subheader(f"Question {st.session_state.index + 1} sur {len(questions)}")

    # Affichage des réponses
    st.session_state.selected = st.radio(
        label=q["question"],
        options=q["options"],
        index=None,
        key=f"radio_{st.session_state.index}"
    )

    # Bouton de validation
    if st.button("✅ Valider ma réponse"):
        st.session_state.show_feedback = True
        if st.session_state.selected == q["answer"]:
            st.session_state.score += 1

    # Affichage du résultat
    if st.session_state.show_feedback:
        if st.session_state.selected == q["answer"]:
            st.success("Bonne réponse ✅")
        else:
            st.error(f"Mauvaise réponse ❌ La bonne réponse était : {q['answer']}")
        st.info(f"💡 {q['explanation']}")

        if st.button("➡️ Question suivante"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.experimental_rerun()
else:
    st.success(f"🎉 Bravo, tu as terminé le quiz ! Ton score : {st.session_state.score} / {len(questions)}")

    if st.button("🔄 Recommencer"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.experimental_rerun()
