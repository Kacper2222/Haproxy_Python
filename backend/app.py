from flask import Flask
import socket 

app = Flask(__name__)

docker_short_id = socket.gethostname()

@app.route('/')
def checking_backend():
    return f"{docker_short_id}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
