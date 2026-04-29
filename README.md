# AI Assistant

A lightweight AI assistant that generates creative responses and summarizes emails.

## Features
- Creative text generation (temperature = 0.8)
- Email summarization
- Simple web interface

## Tech Stack
- Python (Flask)
- React (frontend)
- OpenAI / LLM API

## Setup

Clone the repository:
git clone <repo-url>
cd OpenAI_apis_ai_assistant

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Add environment variables:
Create a `.env` file and add:
API_KEY=your_api_key_here

Run the app:
python main.py or flask --app main run --debug

## Usage
- Enter a prompt for creative AI responses
- Paste email content to generate summaries

## Configuration
- Temperature is set to 0.8 for more diverse outputs
- Can be adjusted in backend config

## Project Structure
.
├── main.py
├── templates/
├── static/
├── .env
└── requirements.txt

## Notes
- Requires a valid API key
- Not production-ready

## Future Improvements
- Conversation memory
- UI enhancements
- Deployment
