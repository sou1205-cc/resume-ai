from flask import Flask
import PyPDF2

app = Flask(__name__)

@app.route("/")
def home():

    file_path = "resume.pdf"

    text = ""

    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text()

    except:
        return "PDFファイルがありません"

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
        if keyword in text:
            found.append(keyword)

    result = "検出スキル:<br>"

    for item in found:
        result += f"・{item}<br>"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
