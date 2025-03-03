import streamlit as st
import ollama
import chromadb
import numpy as np
import random
from sentence_transformers import SentenceTransformer

# ✅ Load ChromaDB for Memory Storage
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="student_memory")

# ✅ Load Embedding Model for Personalization
embedding_model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# ✅ Define topics for each subject
topic_options = {
    "Mathematics": ["Algebra", "Geometry", "Trigonometry"],
    "Science": ["Motion", "Electricity", "Atoms"],
    "Physics": ["Kinematics", "Laws of Motion", "Work and Energy"],
    "Chemistry": ["Periodic Table", "Acids and Bases", "Chemical Reactions"],
    "Biology": ["Cell Structure", "Genetics", "Evolution"],
    "English": ["Grammar", "Tenses", "Comprehension"],
    "Computer Science": ["Data Structures", "Algorithms", "Programming Basics"]
}

# ✅ Initialize student knowledge for ALL topics dynamically
student_profile = {topic: 0.5 for subjects in topic_options.values() for topic in subjects}

# ✅ AI Tutor Chatbot (Ollama)
def ai_tutor(query):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": query}])
    return response['message']['content']

# ✅ Generate Quiz Questions
def generate_quiz(topic):
    prompt = f"Generate a multiple-choice question on '{topic}' with 4 options (A, B, C, D) and the correct answer."
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# ✅ AI Explains the Topic First
def teach_topic(topic):
    prompt = f"Explain the topic '{topic}' in a simple way for a school student."
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# ✅ Adaptive Learning Decision (RL Model)
def adjust_learning_path(topic, correct):
    factor = 1.1 if correct else 0.8  
    student_profile[topic] = max(0, min(1, student_profile[topic] * factor))  

    if student_profile[topic] > 0.8:
        return "✅ Mastered! Move to the next topic."
    elif student_profile[topic] > 0.5:
        return "🔄 Keep practicing with harder questions."
    else:
        return "❌ Struggling! AI will provide hints and reteach."

# ✅ Define subjects for each grade
subject_options = {
    "6": ["Mathematics", "English", "Science"],
    "7": ["Mathematics", "English", "Science"],
    "8": ["Mathematics", "English", "Physics", "Chemistry", "Biology"],
    "9": ["Mathematics", "English", "Physics", "Chemistry", "Biology"],
    "10": ["Mathematics", "English", "Physics", "Chemistry", "Biology"],
    "11": ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Computer Science"],
    "12": ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Computer Science"]
}

# ✅ Initialize session state to remember progress
if "learning_started" not in st.session_state:
    st.session_state.learning_started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "last_answer_correct" not in st.session_state:
    st.session_state.last_answer_correct = None
if "correct_count" not in st.session_state:  # ✅ Tracks how many correct answers
    st.session_state.correct_count = 0
if "explanation" not in st.session_state:  # ✅ Store explanation so it doesn't disappear
    st.session_state.explanation = None

# ✅ Streamlit UI - AI Tutor Interface
st.title("🎓 AI Tutor - Interactive Learning 🚀")

# 📌 Step 1: Select Grade, Subject, and Topic
grade = st.selectbox("Select Grade", list(subject_options.keys()))
subject = st.selectbox("Select Subject", subject_options[grade])
topic = st.selectbox("Select Topic", topic_options.get(subject, ["General"]))

# 📌 Step 2: AI Directly Teaches the Topic
if st.button("Start Learning"):
    st.session_state.learning_started = True
    st.session_state.current_question = generate_quiz(topic)
    st.session_state.explanation = teach_topic(topic)  # ✅ Store explanation permanently
    st.session_state.correct_count = 0  # ✅ Reset correct answer count

# ✅ If learning has started, continue session even after button clicks
if st.session_state.learning_started:
    st.write("📖 AI Tutor: Teaching the topic...")
    st.write(f"🤖 AI Tutor: {st.session_state.explanation}")

    st.write("📝 AI Tutor: Let's test your understanding!")
    st.write(st.session_state.current_question)

    answer = st.radio("Choose your answer:", ["A", "B", "C", "D"], key="answer")

    if st.button("Submit Answer"):
        correct = random.choice([True, False])  # Simulating AI checking answer
        st.session_state.last_answer_correct = correct  

        if correct:
            st.write("✅ Correct! Well done!")
            st.session_state.correct_count += 1  # ✅ Increase correct answer count
        else:
            st.write("❌ Incorrect. AI will provide hints.")

        # ✅ Adjust Learning Path Based on Answer
        learning_decision = adjust_learning_path(topic, correct)
        st.write(f"📊 AI Decision: {learning_decision}")

        if not correct:
            # ✅ AI Gives a Hint If Student Struggles
            st.write("💡 AI Hint:")
            hint = ai_tutor(f"Give a simple hint for {topic}")
            st.write(hint)

        # ✅ If 3 correct answers, ask if student wants to move on
        if st.session_state.correct_count >= 3:
            st.write("🎉 You've answered 3 questions correctly! Do you want to move to the next topic?")
            if st.button("Yes, Next Topic"):
                st.session_state.learning_started = False  # ✅ Reset everything for new topic
                st.session_state.correct_count = 0
                st.session_state.current_question = None
                st.session_state.explanation = None
                st.experimental_rerun()
            if st.button("No, Continue Practicing"):
                st.session_state.correct_count = 0  # ✅ Reset count but keep learning

        else:
            # ✅ AI Generates Another Question After Answering
            st.session_state.current_question = generate_quiz(topic)
            st.write("🔄 Next Question:")
            st.write(st.session_state.current_question)

st.write("🚀 AI Tutor Ready for Learning!")
