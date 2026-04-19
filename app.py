from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "quizmaster_secret_key_2024"

@app.template_filter('option_letter')
def option_letter(index):
    return chr(65 + index)  # 0->A, 1->B, 2->C, 3->D

QUESTIONS = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer": "Canberra"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["186", "206", "226", "246"],
        "answer": "206"
    },
    {
        "question": "Which country is the largest by land area?",
        "options": ["Canada", "China", "USA", "Russia"],
        "answer": "Russia"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Fe", "Au", "Cu"],
        "answer": "Au"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": "1945"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start():
    shuffled = QUESTIONS.copy()
    random.shuffle(shuffled)
    session["questions"] = shuffled
    session["current"] = 0
    session["score"] = 0
    session["answers"] = []
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = session.get("questions", [])
    current = session.get("current", 0)

    if request.method == "POST":
        selected = request.form.get("answer")
        correct = questions[current]["answer"]
        if selected == correct:
            session["score"] = session.get("score", 0) + 1
        session["answers"] = session.get("answers", []) + [selected]
        session["current"] = current + 1
        return redirect(url_for("quiz"))

    if current >= len(questions):
        return redirect(url_for("result"))

    question = questions[current]
    progress = int(((current) / len(questions)) * 100)
    return render_template(
        "quiz.html",
        question=question,
        question_num=current + 1,
        total=len(questions),
        progress=progress
    )


@app.route("/result")
def result():
    score = session.get("score", 0)
    questions = session.get("questions", [])
    answers = session.get("answers", [])
    total = len(questions)
    percentage = int((score / total) * 100) if total > 0 else 0

    if percentage >= 80:
        feedback = "🏆 Outstanding! You're a General Knowledge Champion!"
        feedback_class = "excellent"
    elif percentage >= 60:
        feedback = "👍 Great job! You have solid general knowledge!"
        feedback_class = "good"
    elif percentage >= 40:
        feedback = "📚 Not bad! A little more reading and you'll ace it!"
        feedback_class = "average"
    else:
        feedback = "💪 Keep practising — every quiz makes you smarter!"
        feedback_class = "poor"

    review = []
    for i, q in enumerate(questions):
        review.append({
            "question": q["question"],
            "correct": q["answer"],
            "selected": answers[i] if i < len(answers) else None,
            "is_correct": answers[i] == q["answer"] if i < len(answers) else False
        })

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage,
        feedback=feedback,
        feedback_class=feedback_class,
        review=review
    )


if __name__ == "__main__":
    app.run(debug=True)
