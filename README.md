# AlgTube

AlgTube is a full-stack web application built with FastAPI that allows users to explore, visualize, and save their favorite algorithms.

Users can:
- Create an account and log in
- Browse algorithm pages
- Run interactive algorithm visualizations
- Save (favorite) algorithms for quick access

## Tech Stack

**Backend**: FastAPI (Python)<br>
**Database**: SQLite (via SQLModel)<br>
**Frontend**: HTML, CSS, JavaScript<br>
**Templating**: Jinja2<br>
**Visualization**: Chart.js

## Dependencies

Install all required dependencies using the following command:
pip install fastapi uvicorn sqlmodel jinja2 python-multipart

### Dependency Breakdown:
**fastapi** – backend web framework<br>
**uvicorn** – server to run the app<br>
**sqlmodel** – database ORM for SQLite<br>
**jinja2** – HTML templating engine<br>
**python-multipart** – required for handling form submissions

## Running the Application

Open a terminal in the project folder and run:
uvicorn main:app

Then open your browser and go to:
http://127.0.0.1:8000

Creating an Account:
Open the application in your browser
Navigate to the register page
Enter a username and password
Submit the form
You will be redirected to the home page

Logging In:
- Go to the login page
- Enter your username and password
- Submit the form
- If correct, you will be redirected to the home page

A cookie is stored in your browser to keep you logged in.

## Site Navigation

### Favoriting Algorithms

Log in or create an account:
- Navigate to an algorithm page
- Click the Favorite button
- The algorithm is saved to your account
- Go to the Favorites page to view saved algorithms

### Running Algorithm Visualizations

Open an algorithm page
- Enter a comma-separated list of numbers
    - *Example:5,3,8,1,2*<br>
- Click Submit
    - The algorithm will animate using the chart on the page

## Database

The app uses SQLite and stores data in a local .db file.

| Tables      | Columns                     |
| ----------- | --------------------------- |
| User        | id, username, password      |
| Favorite    | id, user_id, alg_name       |

If database models change, delete the .db file and restart the app
Passwords are stored in plain text for simplicity
Favorites are linked to users using user_id
