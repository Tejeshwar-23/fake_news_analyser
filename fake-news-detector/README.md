# TruthSense | Fake News Detector

TruthSense is an AI-powered news verification system. Follow these steps to get the application up and running on your local machine.

---

## 🚀 Quick Start: How to Run

### **Step 1: Install Dependencies**
Open your terminal in the `backend/` folder and run:
```bash
pip install -r requirements.txt
```

### **Step 2: Start the Backend Server**
While still in the `backend/` folder, run the following command:
```bash
python dev.py
```
> [!NOTE]
> Keep this terminal open while using the app. The API will be running at `http://127.0.0.1:5000`.

### **Step 3: Open the Frontend**
Go to the `frontend/` folder and open **`index.html`** in your web browser (Chrome, Edge, etc.).

---

## 📂 Project Structure

- **`backend/`**: Contains the Flask API, machine learning models (`.pkl` files), and development scripts.
- **`frontend/`**: Contains the user interface (`index.html`).

## 🛠️ Technology Stack
- **Backend**: Python, Flask, Scikit-learn (SVM Model)
- **Frontend**: HTML5, CSS3, JavaScript
- **Vectorization**: TF-IDF

## 📝 How to Use
1. Enter any news article text into the box on the website.
2. Click **Verify Content**.
3. View the AI's analysis of whether the text appears to be "Fake" or "Real".
