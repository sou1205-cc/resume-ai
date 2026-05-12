from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    resume_text = """
    測量経験3年。
    GIS使用経験あり。
    CAD操作可能。
    """

    keywords = [
        "測量",
        "GIS",
        "CAD",
        "Python",
        "測量士",
        "測量士補"
    ]

    found = []

    for keyword in keywords:
        if keyword in resume_text:
            found.append(keyword)

    result = "検出スキル:<br>"

    for item in found:
        result += f"・{item}<br>"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
