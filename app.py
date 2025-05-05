import streamlit as st
import random

st.set_page_config(page_title="Quiz Économie", page_icon="📚")
st.title("📚 Révision - Économie : Les modes de vente")

# -------------------------------
# Questions (10 questions basées sur ton cours)
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
    {
        "question": "Dans la vente au comptant, quand a lieu le paiement ?",
        "options": ["Avant la livraison", "Après la livraison", "En même temps que la livraison"],
        "answer": "En même temps que la livraison",
        "explanation": "Le paiement et la remise du produit ont lieu au même moment dans la vente au comptant."
    },
    {
        "question": "Quel est le principal inconvénient de la vente par internet ?",
        "options": ["On ne peut pas comparer les produits", "On ne peut pas les essayer", "Les prix sont toujours plus élevés"],
        "answer": "On ne peut pas les essayer",
        "explanation": "On ne peut pas tester ou toucher le produit avant de l’acheter sur internet."
    },
    {
        "question": "Que se passe-t-il si plusieurs personnes veulent le même objet aux enchères ?",
        "options": ["L'objet est vendu au prix de départ", "L'objet revient au plus offrant", "L'objet est attribué au hasard"],
        "answer": "L'objet revient au plus offrant",
        "explanation": "Aux enchères, l’objet est attribué à la personne qui propose le prix le plus élevé."
    },
    {
        "question": "Quand l’acheteur reçoit-il le produit dans une vente à crédit ?",
        "options": ["Après paiement complet", "Avant de payer", "Pendant le paiement"],
        "answer": "Avant de payer",
        "explanation": "L'acheteur reçoit l’objet immédiatement, puis le paie en plusieurs fois."
    },
    {
        "question": "Qu’est-ce qu’une vente par correspondance ?",
        "options": ["Une vente dans un magasin", "Une vente à l’oral", "Une commande à distance"],
        "answer": "Une commande à distance",
        "explanation": "Elle se fait via téléphone, courrier ou internet — sans contact direct avec le vendeur."
    },
    {
        "question": "Quel est l'avantage du leasing ?",
        "options": ["Posséder le bien", "Utiliser un bien sans l’acheter", "Ne rien payer"],
        "answer": "Utiliser un bien sans l’acheter",
        "explanation": "Le leasing permet d’utiliser un objet en échange d’un loyer mensuel, sans l’acheter."
    },
    {
        "question": "Quel est le risque avec une enchère inversée ?",
        "options": ["Payer trop tôt", "Manquer l’achat en attendant trop", "Ne pas avoir de facture"],
        "answer": "Manquer l’achat en attendant trop",
        "explanation": "On attend le prix le plus bas, mais on peut perdre le produit si quelqu’un l’achète avant."
    }
]

# -------------------------------
# Session State
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
# Affichage d’une question
# -------------------------------
if st.session_state.index < len(questions):
    q = questions[st.session_state.index]
    st.subheader(f"Question {st.session_state.index + 1} sur {len(questions)}")

    st.session_state.selected = st.radio(
        label=q["question"],
        options=q["options"],
        index=None,
        key=f"q{st.session_state.index}"
    )

    if st.button("✅ Valider ma réponse"):
        st.session_state.show_feedback = True
        if st.session_state.selected == q["answer"]:
            st.session_state.score += 1

    if st.session_state.show_feedback:
        if st.session_state.selected == q["answer"]:
            st.success("Bonne réponse ✅")
        else:
            st.error(f"Mauvaise réponse ❌ La bonne réponse était : {q['answer']}")
        st.info(f"💡 {q['explanation']}")

        if st.button("➡️ Question suivante"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.rerun()

else:
    st.success(f"🎉 Bravo ! Tu as terminé le quiz.\nTon score : {st.session_state.score} / {len(questions)}")
    if st.button("🔁 Recommencer"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.rerun()
