from flask import Flask
import pdfplumber

app = Flask(__name__)

@app.route("/")
def home():

    text = ""

    try:
        with pdfplumber.open("resume.pdf") as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted

    except:
        return "PDFファイルがありません"

    keywords = [
        "測量",
        "GIS",
        "CAD",
        "測量士",
        "測量士補"
    ]

    found = []

    for keyword in keywords:
        if keyword in text:
            found.append(keyword)

    result = "検出スキル:<br>"

    for item in found:
        result += f"・{item}<br>"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
