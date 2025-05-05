import streamlit as st
import random

st.title("Révision - Économie : Les modes de vente")

questions = {
    "Quelle est la différence entre vente au comptant et vente à crédit ?": "Dans la vente au comptant, le paiement est immédiat. Dans la vente à crédit, le paiement est différé ou échelonné.",
    "Dans quel cas l’acheteur paie sans devenir propriétaire ?": "Dans le leasing.",
    "Quel type de vente permet de comparer rapidement les produits ?": "La vente par internet.",
    "Que se passe-t-il si plusieurs personnes veulent le même objet aux enchères ?": "L'objet est attribué à celui qui fait la meilleure offre.",
    "Dans une vente à crédit, que signifie échéance ?": "C'est la date à laquelle le paiement doit être effectué."
}

question = random.choice(list(questions.keys()))
user_answer = st.text_input(f"Question : {question}")

if user_answer:
    correct = questions[question].lower()
    if user_answer.strip().lower() in correct:
        st.success("Bonne réponse !")
    else:
        st.error(f"Mauvaise réponse. Voici une réponse attendue : {questions[question]}")
