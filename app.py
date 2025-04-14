from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    return round(similarity * 100, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text1 = request.form["text1"]
        text2 = request.form["text2"]
        if text1 and text2:
            result = calculate_similarity(text1, text2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
