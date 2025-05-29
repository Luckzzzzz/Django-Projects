# Django-Projects
Weather App (Django)

Description
A Django web application that fetches real-time weather data for a user-entered city using an external weather API and displays temperature, weather condition, and more.

Features
Input any city to fetch its current weather
Displays temperature, humidity, and description
Clean and simple UI
Requirements
Create a requirements.txt:

Django>=3.0
requests
Install with:

pip install -r requirements.txt
How to Run
Clone the repository or download the project.
Navigate to the weather project directory.
Run migrations:
python manage.py makemigrations
python manage.py migrate
Run the server:
python manage.py runserver
Open in browser: http://127.0.0.1:8000/
Football Player Management System (MyProject10)

Description
A Django-based web application for managing football players, including goalkeepers and field players. It supports insert, update, delete, search, and ranking functionalities, with custom validation using Python classes and error handling.

Features
Insert new players (Goalkeeper or FieldPlayer)
Display all players with performance stats
Search player by ID
Update and delete players
Display best goalkeeper (by stopping rate) and best field player (by goal count)
Custom Python classes: Person, GoalKeeper, FieldPlayer
Error handling via a custom MyError class

Requirements
Add to requirements.txt:

Django>=3.0
Install with:

pip install -r requirements.txt
How to Run
Clone the repository or download MyProject10.
Navigate into the MyProject10 folder.
Run the following:
python manage.py makemigrations
python manage.py migrate
Start the development server:
python manage.py runserver
Use the following routes:
/insert – Add new player
/display – Show all players
/search1 – Search player by ID
/display1 – Show best player stats
/update/<id> – Update player
/delete/<id> – Delete player
