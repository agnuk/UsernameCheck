Hello everyone!)

The Mass Checking Telegram Usernames project is a web application developed using Flask and deployed with Waitress. This tool allows users to efficiently check the availability of multiple Telegram usernames simultaneously, providing a streamlined solution for individuals and businesses looking to secure their desired usernames on the popular messaging platform.

The running version is availble at:

https://usernamecheck.ru

The official place to buy and sell Telegram usernames: https://fragment.com (where we check the availability of usernames)

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


    cd ~
    git clone https://github.com/agnuk/UsernameCheck

I would rename the folder to flask-app   

    mv UsernameCheck flask-app

Set Up a Virtual Environment:


    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install Dependencies:

    pip install -r requirements.txt

Run the Application:



    waitress-serve --host=127.0.0.1 --port=8080 app:app

Access the Application:

Open your web browser and navigate to http://127.0.0.1:8080 to start using the tool.

Okay, now if you do not have nginx server, it should be installed:


Installing Nginx:

Step 1: Install Nginx
Update Package Index:

    sudo apt update

Install Nginx:

    sudo apt install nginx

Check Nginx Status:

After installation, ensure that Nginx is running:


    sudo systemctl status nginx

Step 2: Configure Nginx as a Reverse Proxy

Create an Nginx Server Block:
Create a configuration file for your application:


    sudo nano /etc/nginx/sites-available/myapp.conf

Add the Following Configuration:

Replace your_domain.com with your actual domain or IP address:



    server {
        listen 80;
        server_name your_domain.com www.your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;  # Change port if needed for Waitress
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Enable the Server Block:
Create a symbolic link to enable the configuration:

    sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/

Test the Nginx Configuration:

Ensure there are no syntax errors in your configuration:
bash

    sudo nginx -t

Restart Nginx:

Apply the changes by restarting Nginx:
bash

    sudo systemctl restart nginx


Now, lets make waitress running all the time:

Step 1: Create a Systemd Service File

Open a terminal on your server.

Create a new service file for your Flask application. You can name it waitress.service:
bash

    sudo nano /etc/systemd/system/waitress.service

Add the following configuration to the service file, adjusting paths and user as necessary:


    [Unit]
    Description=Waitress Server for running Flask Application
    After=network.target

    [Service]
    User=your_username          # Replace with your actual username (root in my case)
    Group=www-data              # You can change this if needed
    WorkingDirectory=/path/to/your/flask-app  # Adjust to your app's directory  (/root/flask-app)
    ExecStart=/path/to/your/venv/bin/waitress-serve --host=127.0.0.1 --port=8080 app:app  # Adjust the path to your virtual environment and app
    #(/root/flask-app/venv/bin/waitress-serve in my case)
    Restart=always               # Restart service if it crashes

    [Install]
    WantedBy=multi-user.target




Step 2: Enable and Start the Service
Reload systemd to recognize the new service:
bash

    sudo systemctl daemon-reload

Enable the service to start on boot:
bash

    sudo systemctl enable waitress.service

Start the service immediately:
bash

    sudo systemctl start waitress.service


Step 3: Check the Status of Your Service
To verify that your service is running correctly, use:


    sudo systemctl status waitress.service

This command will show you whether the service is active and running.

Step 4: View Logs for Debugging (if necessary)

If you encounter issues, you can check the logs for more information:
bash

    journalctl -u waitress.service -f


Usage

Enter multiple usernames in the provided input field (one per line).
Click the "Check Availability" button.
View the results displayed on the page, showing which usernames are available or taken.
