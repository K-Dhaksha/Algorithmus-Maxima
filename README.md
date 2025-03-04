# EduAI Tutor - Project Documentation

## Project Overview
EduAI Tutor is an AI-powered **interactive learning assistant** that helps students learn through **personalized tutoring, quizzes, and adaptive feedback.**

### Features:
- **AI Tutor Chatbot** – Answers academic questions using AI.
- **Adaptive Quiz Generation** – Tests student understanding dynamically.
- **Memory Tracking (ChromaDB)** – Adjusts difficulty based on past performance.
- **Progress-Based Learning Paths** – AI adapts explanations based on student struggles.
- **Study Plan Generator** – (Planned for future versions).

## Code Structure & Dependencies

```
eduai-tutor/
│── main.py        # AI Tutor Application
│── requirements.txt  # Dependencies
│── README.md      # Instructions
```

### Dependencies
- **Frontend & Backend:** Streamlit (Python)
- **Database:** ChromaDB (for progress tracking)
- **AI Model:** Mistral (via Ollama)

## Setup & Execution Steps

### 1. Clone the Repository
```bash
git clone https://github.com/K-Dhaksha/Algorithmus-Maxima.git
cd eduai-tutor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt  # Install required libraries
```

### 3. Run the Application
```bash
streamlit run main.py  # Start the AI Tutor UI
```

## Expected Output and Technical Details
- **Run the application** (`streamlit run main.py`).
- **Select your grade, subject, and topic.**
- **AI Tutor teaches the topic with explanations.**
- **Take a quiz and see your progress tracked.**
- **AI adapts learning based on your performance.**

## Additional Requirements or Considerations
- **Ollama** should be installed to run Mistral locally.
- Ensure **ChromaDB** is correctly configured for tracking student progress.
- Future versions may integrate **speech recognition** and **teacher analytics** for better learning insights.

## Future Scope
- **Speech Recognition** – Allow students to talk to the AI tutor.
- **Student Reports** – Teachers can track student progress.
- **Study Plan Generator** – AI-driven learning schedules.

## Contributors
- Dhaksha Kalidoss
- Abinaya S
- Janani S
- Janani Shree
- Janani H







