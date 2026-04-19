# 🧠 Quiz Master — General Knowledge Quiz App

A full-stack web quiz application built with **Python**, **Flask**, **HTML**, and **CSS** as part of Assignment 3 for the Web Programming with Python and JavaScript Lab course.

---

## 📸 Features

- 🏠 **Home Page** with a clean landing screen and Start Quiz button
- ❓ **8 General Knowledge MCQs** with 4 options each
- 🔀 **Shuffled Questions** — different order every round
- 📊 **Progress Bar** tracking question completion
- 🏆 **Result Page** with score, percentage, and personalised feedback
- 📋 **Answer Review** showing correct vs your answers after submission
- 🎨 **Responsive UI** with gradient styling and smooth interactions

---

## 🛠️ Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Backend   | Python 3, Flask   |
| Frontend  | HTML5, CSS3       |
| Templating| Jinja2            |
| Deployment| Render / Gunicorn |

---

## 📁 Project Structure

```
quiz_master/
├── app.py                  # Flask app — routes, logic, session handling
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Home page
│   ├── quiz.html           # Quiz page with MCQ options
│   └── result.html         # Score and answer review page
└── static/
    └── style.css           # All styling
```

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Namanyadav18/quiz-master.git
cd quiz-master
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## ☁️ Deploy on Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) and create a **New Web Service**
3. Connect your GitHub repo
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy** — your live URL will be ready in ~2 minutes

---

## 📊 Scoring & Feedback

| Score       | Feedback                                      |
|-------------|-----------------------------------------------|
| 80% – 100%  | 🏆 Outstanding! You're a GK Champion!         |
| 60% – 79%   | 👍 Great job! You have solid general knowledge |
| 40% – 59%   | 📚 Not bad! A little more reading and you'll ace it |
| 0% – 39%    | 💪 Keep practising — every quiz makes you smarter |

---

## 📚 Course Outcomes Covered

- **CO1** — Understanding the Fundamentals of Web Development
- **CO3** — Building Backend Applications using Python and Flask
- **CO4** — Integrating Frontend and Backend Technologies

---

## Naman Yadav

Made for Assignment 3 — Web Programming with Python and JavaScript Lab
