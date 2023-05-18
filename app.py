from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
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
  },
  {
    "id": 3,
    "title": "Backend Engineer",
    "location": "Nairobi, Kenya",
    "salary": "ksh 369,000"
  },
  {
    "id": 4,
    "title": "CyberSecurity Analyst",
    "location": "Nairobi, Kenya",
    "salary": "ksh 199,000"
  }
]

# to access the job items in json format: REST API, JSON API, API ENDPOINT
@app.route("/api/jobs") #application programming interface
def list_jobs():
  return jsonify(JOBS)



@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs = JOBS,
                        company_name = "KaicyLTD")


if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)