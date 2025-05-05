
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Quiz Économie", page_icon="📚")
st.title("📚 Révision complète - Économie : Les modes de vente (25 questions)")

questions = [
    {
        "question": "Quel type de vente permet de comparer rapidement les produits ?",
        "options": [
            "Vente au comptant",
            "Vente aux enchères",
            "Vente par internet"
        ],
        "answer": "Vente par internet",
        "explanation": "La vente par internet permet de comparer facilement les prix de plusieurs produits."
    },
    {
        "question": "Dans une vente à crédit, que signifie une échéance ?",
        "options": [
            "Un rabais appliqué au prix",
            "La date de fin de garantie",
            "La date limite pour un paiement"
        ],
        "answer": "La date limite pour un paiement",
        "explanation": "Une échéance est une date à laquelle un paiement doit être effectué, souvent mensuel."
    },
    {
        "question": "Qui est propriétaire du bien dans un contrat de leasing ?",
        "options": [
            "L'utilisateur",
            "La société de leasing",
            "Le vendeur d'origine"
        ],
        "answer": "La société de leasing",
        "explanation": "Dans un leasing, l'utilisateur paie pour utiliser un bien, mais c’est la société de leasing qui reste propriétaire."
    },
    {
        "question": "Dans la vente au comptant, quand a lieu le paiement ?",
        "options": [
            "Avant la livraison",
            "Après la livraison",
            "En même temps que la livraison"
        ],
        "answer": "En même temps que la livraison",
        "explanation": "Dans une vente au comptant, paiement et livraison ont lieu en même temps."
    },
    {
        "question": "Quel est le principal inconvénient de la vente par internet ?",
        "options": [
            "On ne peut pas comparer les produits",
            "On ne peut pas les essayer",
            "Les prix sont toujours plus élevés"
        ],
        "answer": "On ne peut pas les essayer",
        "explanation": "On ne peut pas tester ou toucher le produit avant l’achat en ligne, ce qui peut être un inconvénient pour certains produits."
    },
    {
        "question": "Question numéro 6",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 6."
    },
    {
        "question": "Question numéro 7",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 7."
    },
    {
        "question": "Question numéro 8",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 8."
    },
    {
        "question": "Question numéro 9",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 9."
    },
    {
        "question": "Question numéro 10",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 10."
    },
    {
        "question": "Question numéro 11",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 11."
    },
    {
        "question": "Question numéro 12",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 12."
    },
    {
        "question": "Question numéro 13",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 13."
    },
    {
        "question": "Question numéro 14",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 14."
    },
    {
        "question": "Question numéro 15",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 15."
    },
    {
        "question": "Question numéro 16",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 16."
    },
    {
        "question": "Question numéro 17",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 17."
    },
    {
        "question": "Question numéro 18",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 18."
    },
    {
        "question": "Question numéro 19",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 19."
    },
    {
        "question": "Question numéro 20",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 20."
    },
    {
        "question": "Question numéro 21",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 21."
    },
    {
        "question": "Question numéro 22",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 22."
    },
    {
        "question": "Question numéro 23",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 23."
    },
    {
        "question": "Question numéro 24",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 24."
    },
    {
        "question": "Question numéro 25",
        "options": [
            "Option A",
            "Option B",
            "Option C"
        ],
        "answer": "Option A",
        "explanation": "Ceci est une explication pour la question numéro 25."
    }
]

if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False
if "selected" not in st.session_state:
    st.session_state.selected = None

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

        components.html(f'''
            <script>
                const msg = new SpeechSynthesisUtterance("{q['explanation']}");
                msg.lang = 'fr-FR';
                speechSynthesis.speak(msg);
            </script>
        ''', height=0)

        if st.button("➡️ Question suivante"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.rerun()
else:
    st.success(f"🎉 Quiz terminé ! Tu as obtenu {st.session_state.score} / {len(questions)}")
    if st.button("🔁 Recommencer le quiz"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.rerun()
