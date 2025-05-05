import streamlit as st
import random

st.set_page_config(page_title="Quiz Économie", page_icon="📚")
st.title("📚 Révision - Économie : Les modes de vente")

# Liste des questions QCM
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
        "explanation": "L'inconvénient principal est qu'on ne peut pas tester ou toucher le produit avant de l'acheter."
    },
    {
        "question": "Que se passe-t-il si plusieurs personnes veulent le même objet aux enchères ?",
        "options": ["L'objet est vendu au prix de départ", "L'objet est attribué au premier arrivé", "L'objet revient au plus offrant"],
        "answer": "L'objet revient au plus offrant",
        "explanation": "Aux enchères, le bien est attribué à la personne qui fait la meilleure offre."
    },
    {
        "question": "Dans une vente à crédit, quand reçoit-on le produit ?",
        "options": ["Avant le paiement complet", "Après le paiement complet", "Seulement après un acompte"],
        "answer": "Avant le paiement complet",
        "explanation": "L'acheteur reçoit l'objet avant d'avoir terminé de le payer, souvent en plusieurs mensualités."
    },
    {
        "question": "Qu’est-ce qu’une vente par correspondance ?",
        "options": ["Une commande effectuée en magasin", "Une vente aux enchères par téléphone", "Une commande par internet, courrier ou téléphone"],
        "answer": "Une commande par internet, courrier ou téléphone",
        "explanation": "La vente par correspondance se fait à distance, via téléphone, courrier ou internet."
    },
    {
        "question": "Quel est l'avantage du leasing ?",
        "options": ["Posséder le bien rapidement", "Utiliser un bien sans l’acheter", "Ne jamais rien payer"],
        "answer": "Utiliser un bien sans l’acheter",
        "explanation": "Le leasing permet d'utiliser un objet sans en être propriétaire, en payant des mensualités."
    },
    {
        "question": "Quel est le risque avec une vente aux enchères inversées ?",
        "options": ["Payer trop tôt", "Manquer l’enchère en attendant trop", "Ne pas connaître le vendeur"],
        "answer": "Manquer l’enchère en attendant trop",
        "explanation": "Le but est d’attendre le prix le plus bas, mais on risque de perdre l'objet si quelqu’un l’achète avant."
    }
]

# Initialisation des variables de session
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'completed' not in st.session_state:
    st.session_state.completed = False

# Affichage de la question actuelle
if st.session_state.question_index < len(questions):
    q = questions[st.session_state.question_index]
    st.subheader(f"Question {st.session_state.question_index + 1} sur {len(questions)}")
    user_choice = st.radio(q["question"], q["options"], key=f"q{st.session_state.question_index}")

    if st.button("✅ Valider ma réponse"):
        if user_choice == q["answer"]:
            st.success("Bonne réponse ! ✅")
            st.session_state.score += 1
        else:
            st.error("Mauvaise réponse ❌")

        st.info(f"💡 {q['explanation']}")

        if st.button("➡️ Question suivante"):
            st.session_state.question_index += 1
            st.experimental_rerun()
else:
    st.session_state.completed = True

# Résultat final
if st.session_state.completed:
    st.success(f"🎉 Quiz terminé ! Ton score final : {st.session_state.score} / {len(questions)}")
