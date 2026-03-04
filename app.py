import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from DevOps! 🚀</h1><p>Our CI/CD Pipeline successfully deployed this app to Google Cloud Run!</p>"

if __name__ == "__main__":
    # Cloud Run assigns a port dynamically, default is usually 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
