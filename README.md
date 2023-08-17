# LiftLog (WIP)
LiftLog is a tool crafted to support your fitness journey. Track your training progress with ease through a history log and visual graphs. Customize your experience by creating personalized training programs and templates for convenient monitoring.

## Technical
This web application is built with ReactJS and SCSS for the frontend, and Django for the backend. It incorporates user authentication using Allauth. Training data, templates, and user information are stored within a custom model. Access to data and verification is managed via a custom API endpoint. The app boasts a comprehensive feature set, including frontend and backend components, user verification, and the ability to track training progress with graphical representation of achievements.

## Screenshot
![Landingpage Screenshot](https://cdn.discordapp.com/attachments/1076153929693417542/1141733538014703766/landingpagescreen.jpg
)

## Dependencies
The following dependencies are required for this project:
- Django: `pip install django`
- djangorestframework: `pip install djangorestframework`
- django-allauth: `pip install django-allauth`
- django-crispy-forms: `pip install django-crispy-forms`
- crispy-bootstrap4: `pip install crispy-bootstrap4`

## Start developing
- bypass execution policy for current session: `Set-ExecutionPolicy Unrestricted -Scope Process`
- activate env: `.\env\Scripts\activate`
- run server: `python .\manage.py runserver`
