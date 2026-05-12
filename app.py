from flask import Flask
from pdf2image import convert_from_path
import pytesseract

app = Flask(__name__)

@app.route("/")
def home():

    text = ""

    try:
        images = convert_from_path("resume.pdf")

        for image in images:
            text += pytesseract.image_to_string(image, lang="jpn")

    except:
        return "OCR失敗"

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
