import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="AI Quiz Game", layout="wide")

# ---------------- QUESTIONS ----------------
questions = [
    {"question": "What does AI stand for?", "options": ["Artificial Intelligence", "Automated Input", "Advanced Internet", "None"], "answer": "Artificial Intelligence"},
    {"question": "Which language is popular for AI?", "options": ["Python", "HTML", "CSS", "Excel"], "answer": "Python"},
    {"question": "What is ChatGPT?", "options": ["Robot", "AI Model", "Game", "Browser"], "answer": "AI Model"},
    {"question": "What is ML?", "options": ["Machine Learning", "Manual Logic", "Main Loop", "Memory Link"], "answer": "Machine Learning"},
    {"question": "AI needs what to learn?", "options": ["Data", "Water", "Sleep", "Music"], "answer": "Data"},
    {"question": "Which company created ChatGPT?", "options": ["Google", "OpenAI", "Microsoft", "Amazon"], "answer": "OpenAI"},
    {"question": "AI can replace?", "options": ["Repetitive Tasks", "Human Emotions", "Dreams", "None"], "answer": "Repetitive Tasks"}
]

# ---------------- SESSION STATE ----------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "scores" not in st.session_state:
    st.session_state.scores = []

# ---------------- TITLE ----------------
st.title("🎉 Live Quiz Game (150 Participants)")

# ---------------- USER NAME ----------------
name = st.text_input("Enter Your Name to Start")

# ---------------- QUIZ ----------------
user_answers = []
score = 0

if name:
    st.subheader(f"Welcome {name}! 🚀 Start the Quiz")

    for i, q in enumerate(questions):
        st.write(f"Q{i+1}. {q['question']}")

        selected = st.radio(
            "Select your answer:",
            q["options"],
            key=f"q{i}"
        )

        # Instant Feedback
        if selected:
            if selected == q["answer"]:
                st.markdown("<p style='color:green'>✅ Correct</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='color:red'>❌ Wrong (Correct: {q['answer']})</p>", unsafe_allow_html=True)

        user_answers.append(selected)

    # ---------------- SUBMIT ----------------
    if st.button("Submit Quiz"):
        score = sum([1 for i, q in enumerate(questions) if user_answers[i] == q["answer"]])

        st.success(f"🎯 Your Score: {score} / {len(questions)}")

        # Save score
        st.session_state.scores.append({"Name": name, "Score": score, "Time": time.time()})
        st.session_state.submitted = True

# ---------------- LEADERBOARD ----------------
if st.session_state.scores:
    df = pd.DataFrame(st.session_state.scores)

    # Sort by score DESC, time ASC
    df = df.sort_values(by=["Score", "Time"], ascending=[False, True])

    st.subheader("🏆 Leaderboard (Top 10)")

    top10 = df.head(10)
    st.dataframe(top10, use_container_width=True)

    # Top 3
    if len(top10) >= 3:
        st.markdown("---")
        st.markdown("### 🎉 Congratulations to Top 3 Winners!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(f"🥇 {top10.iloc[0]['Name']} ({top10.iloc[0]['Score']})")

        with col2:
            st.info(f"🥈 {top10.iloc[1]['Name']} ({top10.iloc[1]['Score']})")

        with col3:
            st.warning(f"🥉 {top10.iloc[2]['Name']} ({top10.iloc[2]['Score']})")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit for Live Team Fun")
