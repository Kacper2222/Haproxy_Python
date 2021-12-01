from flask import Flask, render_template
import requests

app = Flask(__name__)

websiteToCheck = 'http://172.18.0.4:9090'

@app.route('/healthz')
def healthz(): 
    # return f"Status code: {requests.get(websiteToCheck).status_code}"
    return render_template('healthz.html', statusCode=requests.get(websiteToCheck).status_code)

@app.route('/')
def main():
    return render_template('containerId.html', containerId=requests.get(websiteToCheck).text)

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')