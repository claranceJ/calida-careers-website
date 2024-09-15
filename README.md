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
