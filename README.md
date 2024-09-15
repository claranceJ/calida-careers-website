# Calida-careers-website
🌟 Calida Career Website 🌟

Welcome to Calida Career Website! This is a simple, responsive career web application built with Flask on the backend, and HTML/CSS for the frontend. The application lists jobs across various fields, such as data analysis, software engineering, and cybersecurity. It also provides a simple API for accessing job data in JSON format.
🚀 Overview

Calida Career Website is designed to display job listings dynamically and allow users to view job opportunities. The site is user-friendly, visually appealing, and responsive across devices.
✨ Features

    🌐 Dynamic Job Listings: Display of jobs dynamically through a backend Flask API.
    📄 Responsive Design: Optimized for different screen sizes using HTML and CSS.
    📊 REST API: Access job listings via /api/jobs in JSON format.
    🛠️ Tech Stack: Built using Flask for the backend and HTML/CSS for the frontend.

🛠️ Technologies Used

    Flask: For the backend server and routing.
    HTML5: For structuring the webpage content.
    CSS3: For styling and responsive layout.
    JSON API: Provides an endpoint to serve job data in JSON format.

📋 Installation

To run this project locally:

    Clone the repository:

    bash

git clone https://github.com/your-username/calida-career-website.git

Navigate to the project directory:

bash

cd calida-career-website

Set up a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

bash

pip install -r requirements.txt

Run the Flask app:

bash

python app.py

Open your browser and visit:

bash

    http://127.0.0.1:5000

🖥️ Folder Structure

php

Calida Career Website/
├── static/
│   ├── css/
│   │   └── styles.css  # CSS styling
├── templates/
│   └── home.html  # HTML template for the homepage
├── app.py  # Flask backend logic
└── requirements.txt  # Python dependencies

📑 API

This project also exposes a REST API:

    GET /api/jobs: Returns all available jobs in JSON format.

Example Response:

json

[
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Nairobi, Kenya",
    "salary": "ksh 320,000"
  },
  {
    "id": 2,
    "title": "Frontend Engineer",
    "location": "Nairobi, Kenya",
    "salary": "ksh 216,000"
  }
]

🎨 Frontend Details

HTML (home.html)

html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/styles.css">
    <title>Calida Career Website</title>
</head>
<body>
    <header>
        <h1>Welcome to {{ company_name }}</h1>
        <p>Find your dream job today!</p>
    </header>

    <section class="jobs-list">
        <h2>Available Jobs:</h2>
        <ul>
            {% for job in jobs %}
            <li>
                <h3>{{ job.title }}</h3>
                <p>Location: {{ job.location }}</p>
                <p>Salary: {{ job.salary }}</p>
            </li>
            {% endfor %}
        </ul>
    </section>
</body>
</html>

CSS (styles.css)

css

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    color: #333;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 10px 0;
    text-align: center;
}

.jobs-list {
    margin: 20px;
}

.jobs-list ul {
    list-style-type: none;
    padding: 0;
}

.jobs-list li {
    background: white;
    margin: 10px 0;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.jobs-list h3 {
    margin: 0;
    font-size: 1.2em;
}

🤝 Contributing

Contributions are always welcome! If you have any suggestions or improvements, feel free to fork this repository and submit a pull request.

    Fork the repository
    Create a new branch:

    bash

git checkout -b feature/your-feature-name

Make your changes
Commit your changes:

bash

git commit -m 'Add some feature'

Push to the branch:

bash

    git push origin feature/your-feature-name

    Open a pull request

📞 Contact

If you have any questions or feedback, please feel free to reach out:

    📧 Email: jacktonec@gmail.com
    🔗 LinkedIn: Jacktone Clarance
