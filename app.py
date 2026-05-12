from flask import Flask
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": """
                この応募者を簡潔に要約してください。

                測量経験3年。
                GIS使用経験あり。
                CAD操作可能。
                """
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
