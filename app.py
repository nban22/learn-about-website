from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,000,000'
  },
  {
    'id': 3,
    'title': 'Fontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 15,000,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Viet Nam',
    'salary': '15,000,000vnd'
  },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = 'An đẹp zai')

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  