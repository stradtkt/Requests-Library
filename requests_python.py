from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
  request = requests.get('https://api.github.com/users/stradtkt/repos')
  commits = requests.get('https://api.github.com/repos/stradtkt/algorithms/commits')
  return render_template('index.html', request=request.json()[2], commits=commits.json())

app.run(debug=True)