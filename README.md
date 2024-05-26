# To-Do List App

This is a simple To-Do List application built with Flask and SQLAlchemy.

## Features

- Add tasks
- Edit tasks
- Mark tasks as complete or incomplete
- Delete tasks
- Filter tasks by completion status

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Diorski/to_do_list_app.git
    cd to_do_list_app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000/`.

## Running Tests

To run the unit tests:
```bash
python -m unittest discover tests
