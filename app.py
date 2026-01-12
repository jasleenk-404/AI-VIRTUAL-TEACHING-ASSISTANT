# from flask  import Flask, render_template, request
# from assistant import answer_question
# from quiz import get_quiz, evaluate_answer

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get", methods=["POST"])
# def get_response():
#     user_question=request.form["msg"]

#     if user_question.lower()=="start quiz":
#         quiz= get_quiz()
#         question_text = ""
#         for qid, qdata in quiz.items():
#             question_text += qdata["question"] + " Options:" + ",".join(qdata["options"]) + "\n"
#             return question_text
        
#         return answer_question(user_question)

   

# if __name__== "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
from assistant import answer_question
from quiz import get_quiz, evaluate_answer
from datetime import datetime
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat_page")
def chat_page():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_question = request.form["msg"]
    response = answer_question(user_question)
    return render_template("chat.html", response = response)

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = get_quiz()
    if request.method =="POST":
        score = 0
       

        for qid in questions:
            user_answer= request.form.get(qid)
            if user_answer and evaluate_answer(qid,user_answer):
                score += 1
        return render_template("result.html", score = score)
  
    return render_template("quiz.html", questions= questions)


@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    questions = get_quiz()
    score = 0

    for qid in questions:
        user_answer = request.form.get(qid)
        if user_answer and evaluate_answer(qid, user_answer):
            score += 1

        with open("data/quiz_results.csv", "a", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(),score, len(questions)])

                

    return render_template("result.html", score=score, total=len(questions))

if __name__ == "__main__":
    app.run(debug=True)
