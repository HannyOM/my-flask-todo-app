# Flask Todo Application

A basic Todo application made with flask to help track your tasks.

## Requirements:

NOTE: For any installation you do not know yet, please check YouTube for a video tutorial.

You should have installed:

- Python 3.13.2 (or the latest python)
- Visual Studio Code (or any other IDE e.g Pycharm, Atom)

## Process:

1. Create a folder to contain the entire project. Here, I used the name "my-flask-todo-app".

2. Access the folder "my-flask-todo-app" in the terminal and create a virtual environment by running the syntax below:

   `python -m venv virtual_env`

3. Activate the virtual environment. If you are currently within the main directory (the "my-flask-todo-app" folder) in your terminal, then run:

   `.\virtual_env\Scripts\activate`

4. After activating your virtual environment, install the necessary libraries by running the code below:

   `pip install requirements.txt`

5. Now run the following:

   `set FLASK_APP=app.py`

   `set FLASK_ENV=development`

   `flask run`

## Suggestions for Improvement:

1. Add date and time tracking.
2. Add notifications for reminders.
3. Add caller agent for better reminders.
