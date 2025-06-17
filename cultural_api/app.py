# app.py

from flask import Flask
from routes.greeting_route import greeting_bp

app = Flask(__name__)
app.register_blueprint(greeting_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
