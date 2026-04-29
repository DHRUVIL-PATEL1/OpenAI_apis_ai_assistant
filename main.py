from flask import Flask, render_template, url_for, jsonify, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") # API KEY

app = Flask(__name__)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

@app.route("/")
def main():
  return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():

  data = request.get_json()

  question = data.get("question")

  if not question:
    return jsonify({"answer": "No question provided"}), 400

  response = client.responses.create(
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Answer in a bit creative manner"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": question
                        }
                    ]
                }
            ],
            model="openai/gpt-oss-20b",
            max_output_tokens=128,
            temperature=0.9
        )
  
  answer = response.output[1].content[0].text

  return jsonify({"answer": answer})

@app.route("/summarize", methods=["POST"])
def summarize():
  
    data = request.get_json()
    email = data.get("email")

    summary_response = client.responses.create(
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Act like an expert email summarizer and summarize the given email in 2 lines"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": email
                    }
                ]
            }
        ],
        model="openai/gpt-oss-20b",
        max_output_tokens=128,
        temperature=0.1
    )

    answer = summary_response.output[1].content[0].text

    return jsonify({"answer": answer})
# @app.route("/summarize")
# def summarize():
#   return