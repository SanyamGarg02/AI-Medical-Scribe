# AI-Medical-Scribe

This Streamlit web app allows users to record medical speech, transcribe it using OpenAI Whisper, and format it into professional medical note types such as SOAP, BIRP, DAP, Progress, or Operative Notes.

---

## ✨ Features

- 🎙️ Record audio input via microphone
- 🧠 Transcribe audio using OpenAI Whisper
- 📝 Format transcriptions into structured medical notes using GPT-4
- 🩺 Supports multiple formats: SOAP, BIRP, DAP, Progress, and Operative Notes

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- OpenAI Python SDK
- SpeechRecognition
- wave
- pyaudio
- python-dotenv

Install them using:

```bash
pip install -r requirements.txt

#Setup API Key
1.Create a .env file in the project root:
    -paste inside .env: OPENAI_API_KEY=your-openai-api-key-here

2. Run using this:
    -streamlit run main.py
```
