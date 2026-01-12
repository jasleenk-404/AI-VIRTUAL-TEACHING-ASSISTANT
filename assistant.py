import csv
from datetime import datetime
import os
def detect_intent(question):
    question = question.lower()

    if any(word in question for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in question for word in ["deadline", "submission", "last date"]):
        return "deadline"

    elif any(word in question for word in ["quiz", "test", "exam"]):
        return "quiz"

    elif any(word in question for word in ["admission", "apply", "enrollment"]):
        return "admission"
    
    elif any(word in question for word in["syllabus","topics","course content"]):
        return "syllabus"
    
    elif any(word in question for word in ["attendance", "present","absent"]):
        return "attendance"
    
    elif any(word in question for word in["class","schedule","timing"]):
        return "class_schedule"
    
    elif any(word in question for word in["study","prepare","how to learn"]):
        return "study_help"
    
    elif any(word in question for word in["stress","worried","fail","nervous"]):
        return "motivation"
    
    elif any(word in question for word in["contact","faculty","teacher","information"]):
        return "contact"
    
    else:
        return "unknown"


def answer_question(question):
    intent = detect_intent(question)

    if intent == "greeting":
        return "Hello! I am your AI Virtual Teaching Assistant. How can I assist you?"
    
    elif intent== "syllabus":
        return "The syllabus includes python, DSA, AI basics, Basic Calculus and Algebra, and Flask."
    
    elif intent=="attendance":
        return "Minimum 75% attendance is required to appear for exams"
    
    elif intent== "class_schedule":
        return "Classes are held from 9 AM to 5 PM,Monday to Friday.Suitable Timetable for lectures will be provided in respective student portal."
    
    elif intent== "study_help":
        return "I recommend revising lecture notes, practicing questions, and attempting mock tests.If you can arrange PYQs that would be Awesome."
    
    elif intent== "motivation":
        return "Don't worry.Stay consistent, practice regularly, and ask for help whenever needed."
    
    elif intent== "quiz":
        return "Quiz/Exam will be taken tomorrow on the respective student portal."
    
    elif intent== "contact":
        return "You can contact through official email or LMS."

    elif intent == "deadline":
        return "The next assignment deadline is 15 January."

    elif intent == "quiz":
        return "The quiz will be available on the student portal."

    elif intent == "admission":
        return "For admission related queries, please contact the Admission Office at admission@college.edu or call +91-XXXXXXXXXX."

    else:
        return "I am still learning. Please ask something related to academics."
# import csv
# from datetime import datetime

# def answer_question(question):
#     answers = {
#         "what is ai": "AI stands for Artificial Intelligence.",
#         "what is machine learning": "Machine Learning is a subset of AI.",
#         "what is deep learning": "Deep Learning uses neural networks."
#     }

#     response = answers.get(question.lower(), "Sorry, I don't know the answer yet.")

    save_chat(question, response)
    return response


def save_chat(question, response):
    os.makedirs("data", exist_ok=True)

    with open("data/chat_history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell()== 0:
            writer.writerow(["Timestamp","Question","Response"])
        writer.writerow([datetime.now(), question, response])