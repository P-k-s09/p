# Plagiarism Detector Website

This is a simple web application that detects similarity between two text inputs using cosine similarity and TF-IDF.

## Features

- Paste two texts and compare their similarity.
- Powered by Flask and scikit-learn.

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plagiarism-detector.git
   cd plagiarism-detector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Deploy on Render

1. Go to [https://render.com](https://render.com)
2. Create a new Web Service and connect this repo.
3. Set the build command to:
   ```
   pip install -r requirements.txt
   ```
4. Set the start command to:
   ```
   python app.py
   ```
5. Add an environment variable:
   ```
   Key: PORT
   Value: 5000
   ```

## Live Demo

[Link will go here after deployment]
