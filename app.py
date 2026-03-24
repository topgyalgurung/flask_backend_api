
from flask import Flask

app = Flask(__name__) # set Flask app instance
    # __name__ help Flask locate resources

@app.route('/')

def hello():
    return "Hello, Flask"

# debug provide detailed error message, server auto reload etc
if __name__ == "__main__":
    app.run(debug=True)