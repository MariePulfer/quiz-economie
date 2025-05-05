import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Quiz Économie", page_icon="📚")
st.title("📚 Révision - Économie : Les modes de vente")

# -------------------------------
# Liste des 15 questions
# -------------------------------
questions = [
    {
        "question": "Quel type de vente permet de comparer rapidement les produits ?",
        "options": ["Vente au comptant", "Vente aux enchères", "Vente par internet"],
        "answer": "Vente par internet",
        "explanation": "La vente par internet permet de comparer facilement les prix de plusieurs produits, ce qui est son avantage principal."
    },
    {
        "question": "Dans une vente à crédit, que signifie une échéance ?",
        "options": ["Un rabais appliqué au prix", "La date de fin de garantie", "La date limite pour un paiement"],
        "answer": "La date limite pour un paiement",
        "explanation": "Une échéance est une date à laquelle un paiement doit être effectué, souvent mensuel, dans le cadre d’un crédit."
    },
    {
        "question": "Qui est propriétaire du bien dans un contrat de leasing ?",
        "options": ["L'utilisateur", "La société de leasing", "Le vendeur d'origine"],
        "answer": "La société de leasing",
        "explanation": "Dans un leasing, l'utilisateur paie pour utiliser un bien, mais c’est la société de leasing qui reste propriétaire."
    },
    {
        "question": "Dans la vente au comptant, quand a lieu le paiement ?",
        "options": ["Avant la livraison", "Après la livraison", "En même temps que la livraison"],
        "answer": "En même temps que la livraison",
        "explanation": "Dans une vente au comptant, paiement et livraison ont lieu en même temps."
    },
    {
        "question": "Quel est le principal inconvénient de la vente par internet ?",
        "options": ["On ne peut pas comparer les produits", "On ne peut pas les essayer", "Les prix sont toujours plus élevés"],
        "answer": "On ne peut pas les essayer",
        "explanation": "L'inconvénient majeur de la vente en ligne est qu'on ne peut pas tester ou essayer le produit avant l'achat."
    },
    {
        "question": "Que se passe-t-il si plusieurs personnes veulent le même objet aux enchères ?",
        "options": ["L'objet est vendu au prix de départ", "L'objet revient au plus offrant", "L'objet est attribué au hasard"],
        "answer": "L'objet revient au plus offrant",
        "explanation": "Lors d'une enchère classique, l'objet est attribué à la personne qui propose l'offre la plus élevée."
    },
    {
        "question": "Quand l’acheteur reçoit-il le produit dans une vente à crédit ?",
        "options": ["Après paiement complet", "Avant de payer", "Pendant le paiement"],
        "answer": "Avant de payer",
        "explanation": "Dans une vente à crédit, le client reçoit le bien avant d’avoir payé la totalité du prix."
    },
    {
        "question": "Qu’est-ce qu’une vente par correspondance ?",
        "options": ["Une vente dans un magasin", "Une vente à l’oral", "Une commande à distance"],
        "answer": "Une commande à distance",
        "explanation": "La vente par correspondance est une vente à distance effectuée par internet, téléphone ou courrier."
    },
    {
        "question": "Quel est l'avantage du leasing ?",
        "options": ["Posséder le bien", "Utiliser un bien sans l’acheter", "Ne rien payer"],
        "answer": "Utiliser un bien sans l’acheter",
        "explanation": "Le leasing permet d'utiliser un bien moyennant un loyer, sans en être propriétaire."
    },
    {
        "question": "Quel est le risque avec une enchère inversée ?",
        "options": ["Payer trop tôt", "Manquer l’achat en attendant trop", "Ne pas avoir de facture"],
        "answer": "Manquer l’achat en attendant trop",
        "explanation": "Dans les enchères inversées, le prix diminue mais on peut rater l'achat si quelqu'un clique avant nous."
    },
    {
        "question": "Qu’est-ce que la vente à terme implique ?",
        "options": ["Paiement immédiat", "Livraison différée", "Paiement différé ou échelonné"],
        "answer": "Paiement différé ou échelonné",
        "explanation": "La vente à terme permet de recevoir le produit tout de suite, mais de le payer plus tard ou en plusieurs fois."
    },
    {
        "question": "Pourquoi une vente aux enchères peut-elle avoir lieu ?",
        "options": ["Pour aider un commerçant", "Pour vendre un bien saisi ou hérité", "Pour échanger des services"],
        "answer": "Pour vendre un bien saisi ou hérité",
        "explanation": "Les ventes aux enchères ont souvent lieu pour liquider des biens saisis ou issus d'une succession."
    },
    {
        "question": "Qu’est-ce qu’une vente aux enchères inversée ?",
        "options": ["Le prix augmente", "On paie avant de voir le produit", "Le prix baisse jusqu’à un achat"],
        "answer": "Le prix baisse jusqu’à un achat",
        "explanation": "Dans une enchère inversée, le prix diminue et le premier à accepter remporte le produit."
    },
    {
        "question": "Comment s’effectue la vente par correspondance ?",
        "options": ["Par téléphone, courrier ou internet", "Par livraison en main propre", "Sur un stand de rue"],
        "answer": "Par téléphone, courrier ou internet",
        "explanation": "Ce type de vente se fait à distance, sans contact direct avec le vendeur."
    },
    {
        "question": "Quelle est la principale caractéristique du leasing ?",
        "options": ["C’est un prêt gratuit", "C’est un paiement sans contrat", "C’est un droit d’usage sans propriété"],
        "answer": "C’est un droit d’usage sans propriété",
        "explanation": "Le leasing est un contrat de location où le client n’est pas propriétaire du bien."
    }
]

# -------------------------------
# Initialisation de la session
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
# Affichage des questions
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

        # Lecture automatique de l'explication
        components.html(f"""
            <script>
                const msg = new SpeechSynthesisUtterance("{q['explanation']}");
                msg.lang = 'fr-FR';
                speechSynthesis.speak(msg);
            </script>
        """, height=0)

        if st.button("➡️ Question suivante"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.rerun()

# -------------------------------
# Résultat final
# -------------------------------
else:
    st.success(f"🎉 Bravo, tu as terminé le quiz !\nTon score : {st.session_state.score} / {len(questions)}")
    if st.button("🔁 Recommencer le quiz"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.rerun()
