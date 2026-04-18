from google import genai
from dotenv import load_dotenv
import os , io
from gtts import gTTS 
import streamlit as st

load_dotenv()

my_api_key = os.getenv("GEMiNI_API")

client  = genai.Client(api_key=my_api_key)
def node_generate(images):
    prompt =  """Summarize the picture in note format in language Bangla at max 100 words
    make sure to add necessary markdown to differentiate different section"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text
def audio_transscription (text) :
    spech = gTTS(text,lang="en")
    spech.save('hello.mp3')

def audio_transcription(text):
    speech = gTTS(text,lang='bn',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image,difficulty):

    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 