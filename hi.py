import openai
import streamlit as st
import speech_recognition as sr
import wave
import os

from dotenv import load_dotenv
load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
def record_audio(filename="input.wav"):
    """Record audio and save it to a file."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=60)  # Adjust for background noise
        st.write("Listening...")
        audio = recognizer.listen(source)  # Capture audio input
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio.get_wav_data())
    st.success("Recording complete.")
def transcribe_audio(filename="input.wav"):
    """Transcribes recorded audio using OpenAI Whisper."""
    with open(filename, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    return response['text']
def format_transcription(text, format_type):
    """Formats the transcription into the selected medical note format."""
    prompt = f"Convert the following patient transcript into {format_type} format:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a medical assistant helping to structure patient notes."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
# Streamlit UI

st.title("Medical Speech-to-Text Notes Formatter")
note_format = st.selectbox("Select Note Format", ["SOAP Notes", "BIRP Notes", "DAP Notes", "Progress Notes", "Operative Notes"])
if st.button("Record Audio"):
    record_audio()
    st.write("Audio recorded. Click 'Transcribe' to generate text.")
if st.button("Transcribe and Format"):
    transcript = transcribe_audio()
    formatted_text = format_transcription(transcript, note_format)
    st.text_area("Formatted Notes:", formatted_text, height=300)