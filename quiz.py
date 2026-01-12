# quiz.py

quiz_questions = {
    "q1": {
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "Automated Interface", "Advanced Internet"],
        "answer": "Artificial Intelligence"
    },
    "q2": {
        "question": "Which language is used for Flask?",
        "options": ["Java", "Python", "C++"],
        "answer": "Python"
    },
    "q3":{
        "question": "what is flask?",
        "options": ["web framework","Database","Operating System"],
        "answer": "web framework"
    },
    "q4":{
        "question": "What is largest Democracy?",
        "options":["India","US","Italy"],
        "answer": "India"
    },
    "q5":{
        "question":"when is valentine day in february",
        "options":["20","12","14"],
        "answer": "14"
    }
}

def get_quiz():
    return quiz_questions

def evaluate_answer(question_id, user_answer):
    correct_answer = quiz_questions[question_id]["answer"]
    if user_answer == correct_answer:
        return True
    else:
        return False