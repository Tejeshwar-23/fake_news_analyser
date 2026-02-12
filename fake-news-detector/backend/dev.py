import sys
import os

# Add the current directory to sys.path so we can import from api/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'api')))

from predict import app

if __name__ == "__main__":
    print("Starting local development server for preview...")
    print("API will be available at http://127.0.0.1:5000/api/predict")
    app.run(debug=True, port=5000)
