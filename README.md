STUDY TRACKER

Study Tracker is a Django web application that helps users manage their study subjects and track daily progress.
Each user can add subjects, set a daily study goal, and record their study sessions to monitor consistency and improvement over time.

FEATURES
- User authentication (only logged-in users can manage their subjects and study time)
- Add, edit, and delete study subjects with daily goals
- Log study sessions in minutes
- Automatic calculation of total study time
- Form and model validation for clean data
- Class-based and function-based views
- Comprehensive unit tests for models, forms, and views

TECH STACK
- Backend: Django 5.x (Python 3.12)
- Frontend: Django templates (HTML, CSS)
- Database: PostgreSQL
- Authentication: Django’s built-in user system
- Testing: Django TestCase and unittest

INSTALLATION

- Clone the repository:
git clone https://github.com/yourusername/study-tracker.git
cd study-tracker
- Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
- Install dependencies:
pip install -r requirements.txt
- Apply migrations:
python manage.py migrate
- Run the development server:
python manage.py runserver
- Open the app in your browser:
http://127.0.0.1:8000/

USAGE

- Register or log in to your account.
- Add subjects and set daily goals (e.g., 60 minutes for “Math”).
- Log study sessions as you complete them.
- View total study time and update your goals when needed.

RUNNING TESTS

To run all tests:
python manage.py test

The test suite covers:
- Model validation (subjects, edited goals, study progress)
- Form validation (add/edit subject forms)
- View logic (adding, deleting, and updating subjects)
- Key Learnings

THIS PROJECT DEMONSTRATES
- How to build and structure a Django web application from scratch
- Using class-based views effectively
- Writing form and model validation
- Building a test-driven Django project
- Implementing authentication and user-specific data handling

FUTURE IMPROVEMENTS
- Add study statistics and charts (e.g., with Chart.js or Plotly)
- Add streak tracking and motivation messages
- User profile customization
- Deployment to a public hosting platform (e.g., Render, Railway, or Heroku)

Author

Ivan Goranov
- Application Manager and Aspiring Software Engineer
- LinkedIn https://www.linkedin.com/in/ivan-goranov-323618170/
