from flask import Flask

app = Flask(__name__)

# basic python flask server
@app.route("/")
def get():
    return {'oracle': 'python'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')