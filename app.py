from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        data = {"message": "hello there"}
        return f"<h1>Gateway Active</h1><p>Backend says: {data['message']}</p>"
    except Exception as e:
        return f"<h1>Gateway Error</h1><p>Could not reach VM 2: {str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
