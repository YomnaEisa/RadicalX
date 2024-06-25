# Gemini Quizzify
This project addresses the lack of accessible and effective methods for students and learners to reinforce their understanding 
of various topics. The AI-generated assessment and quiz tool provides instant feedback and comprehensive explanations, 
facilitating deeper comprehension and retention of knowledge. By dynamically generating quizzes based on user-provided documents,
ranging from textbooks to scholarly papers, the tool offers a tailored learning experience.
The end result is a user-friendly platform that empowers individuals to hone their skills, solidify their understanding, 
and ultimately excel in their academic pursuits.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)

## Features
1. Dynamic Quiz Generation: Generate quizzes from user-provided documents, including textbooks and scholarly papers.
2. Instant Feedback: Receive immediate feedback on quiz responses.
3. Comprehensive Explanations: Access detailed explanations for each quiz question.
4. Tailored Learning Experience: Personalized quizzes based on the document provided.
5. User-Friendly Interface: An easy-to-use platform for seamless interaction.

## Installation

1. Clone the Repository

```bash
git clone https://github.com/YomnaEisa/RadicalX/tree/main/Mission2%20-%20Gemini%20Quizzify.git
cd Mission2 - Gemini Quizzify/mission-quizify
```

2. Create a Virtual Environment:
```bash
python3 -m venv venv
source venv\Scripts\activate
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the Streamlit Application:
```bash
streamlit run task_10.py
```

## Project Structure
### Project Structure
1. tasks/task_3: Document processing logic.
2. tasks/task_4: Embedding client for handling text embeddings.
3. tasks/task_5: Chroma collection creation.
4. tasks/task_8: Quiz generation logic.
5. tasks/task_9: Quiz management logic.
6. tasks/task_10: Main application script for Streamlit.
