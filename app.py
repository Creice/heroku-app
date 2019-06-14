# Dies ist ein Python 3 Skript!
from flask import Flask
app = Flask(__name__)
# Wir schreiben hier einen Server!
#decorator
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/goodbye')
def goodbye():
    return 'Au revoir monde'
