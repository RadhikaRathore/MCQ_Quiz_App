# MCQ_Quiz_App
A Python Django Web Application for taking MCQ (Multiple choice questions) tests.

### About
This application is developed in Python Django, Where a user can sign in with any of the one roles "teacher" or "student".
A teacher can make new quizzes while a student can take quizzes related to their interests.

### Running Application Locally

* First, clone the repository to your local machine
* Install the requirements:

```bash
pip install -r requirements.txt
```

* Create the database:

```bash
python manage.py migrate
```

* Run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
