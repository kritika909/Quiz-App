# Quiz-App
A dynamic web-based quiz application built using Django. This application allows users to attempt quizzes, tracks their performance, and provides detailed feedback on their answers.

## Features

* User authentication (Login/Signup).

* Real-time answer submission.

* Automatic session tracking for quiz attempts.

* Detailed result analysis including:
      * Total marks.
      * Number of correct and incorrect answers.

* Secure and user-friendly interface.

* Randomized question order to enhance test fairness.

## Technologies Used

* Backend: Django (Python)
* Frontend: HTML, CSS
* Database: SQLite (default Django database, can be replaced with PostgreSQL or MySQL)

## Installation
```
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
```

## Prerequisites
* Python (>= 3.8)
* pip (Python package manager)
* Virtualenv (optional but recommended)

## Steps

### Clone the Repository:
``` python
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
```

### Set Up Virtual Environment:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### Install Dependencies:
```
pip install -r requirements.txt
```
### Apply Migrations:
```
python manage.py migrate
```
### Create a Superuser (for admin panel access):
```
python manage.py createsuperuser
```
### Run the Development Server:
```
python manage.py runserver

Visit http://127.0.0.1:8000 to view the application.
```
## Usage

### Admin Panel:

* Login to the admin panel at http://127.0.0.1:8000/admin.
* Create quizzes, questions, and manage user sessions.

### User Flow:
* Users can register, log in, and view available quizzes.
* Attempt a quiz and submit answers.
* View detailed results after quiz completion.



## Models

### 1. Quiz
`id: Primary key`

`name: Name of the quiz`

`numofques: Number of questions in the quiz`

### 2. Question
`id: Primary key`

`quizid: Foreign key to Quiz`

`ques: The question text`

`optionA, optionB, optionC, optionD: Answer options`

`ans: Correct answer`

`marks: Marks for the question`

### 3. Session

`id: Primary key`

`userid: Foreign key to User`

`quizid: Foreign key to Quiz`

`correct_ans, incorrect_ans, total_marks: Performance tracking`

### 4. Answers

`id: Primary key`

`sessionid: Foreign key to Session`

`ques: Question text`

`user_ans: User's selected answer`

`corr_ans: Correct answer`

## Future Enhancements
* Add a timer for quizzes.
* Include analytics for users to track progress.
* Leaderboard
* Implement question categories and difficulty levels.
* Mobile app integration.
