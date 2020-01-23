from flask import Flask
from App import *

app = Flask(__name__, template_folder='App/views')
app.config['SECRET_KEY'] = 'mykey'
app = Route().map(app)

if __name__ == '__main__':
    app.run(debug=True)
