Hello everyone!)

The Mass Checking Telegram Usernames project is a web application developed using Flask and deployed with Waitress. This tool allows users to efficiently check the availability of multiple Telegram usernames simultaneously, providing a streamlined solution for individuals and businesses looking to secure their desired usernames on the popular messaging platform.

The running version is availble at:

Usernamecheck.ru

Features

Batch Username Checking: Users can input a list of usernames to check their availability in bulk, saving time compared to manual checks.
Real-Time Results: The application provides immediate feedback on the status of each username, indicating whether it is available or already taken.
User-Friendly Interface: Built with a clean and intuitive web interface, making it accessible for users of all technical levels.
Flask Framework: Leveraging Flask's robust capabilities for web development, ensuring a scalable and maintainable codebase.
Waitress Deployment: Utilizes Waitress as the WSGI server for serving the application, ensuring reliability and performance.

Technical Details

Backend: The application is built using Python with the Flask framework. It handles user requests, processes username checks, and serves results dynamically.
Frontend: The user interface is designed using HTML and CSS, providing an engaging experience for users submitting username requests.
Deployment: The application runs on a server configured with Waitress, allowing it to handle multiple requests efficiently.

Installation process:

Installation Instructions

To set up the project locally, follow these steps:

Clone the Repository:

bash
"git clone https://github.com/agnuk/UsernameCheck"
"cd UsernameCheck"

Set Up a Virtual Environment:

bash
"python3 -m venv venv"
"source venv/bin/activate  # On Windows use `venv\Scripts\activate`"


Install Dependencies:

bash
"pip install -r requirements.txt"

Run the Application:

bash

"waitress-serve --host=127.0.0.1 --port=8080 app:app"

Access the Application:

Open your web browser and navigate to http://127.0.0.1:8080 to start using the tool.

Okay, now if you do not have nginx server, it should be installed:






Usage

Enter multiple usernames in the provided input field (one per line).
Click the "Check Availability" button.
View the results displayed on the page, showing which usernames are available or taken.
