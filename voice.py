import os
import threading
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()
# Replace 'YOUR_NEW_API_KEY' with your actual API key
genai.configure(api_key="AIzaSyAPwcYl2lnfD9JBSjl6CTz08SuYABrBo7g")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[]
)

def recognize_speech():
    def listen_and_recognize():
        with sr.Microphone() as source:
            status_label.config(text="Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            status_label.config(text="Listening...")
            try:
                audio = recognizer.listen(source, timeout=10)  # Set timeout for listening
                status_label.config(text="Recognizing...")
                text = recognizer.recognize_google(audio)
                conversation_text.insert(tk.END, "You said: " + text + "\n")
                inst = "Instruction: Act as Doctor, reply to patient in a soft tone."
                qfromuser = inst + text
                response = chat_session.send_message(qfromuser)
                conversation_text.insert(tk.END, "Response: " + response.text + "\n")
                engine = pyttsx3.init()
                engine.say(response.text)
                engine.runAndWait()
                status_label.config(text="Done")
            except sr.UnknownValueError:
                status_label.config(text="Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                status_label.config(text="Could not request results; {0}".format(e))
            except sr.WaitTimeoutError:
                status_label.config(text="Listening timed out, please try again.")

    # Run the listening in a separate thread
    threading.Thread(target=listen_and_recognize).start()

# Create the main window
root = tk.Tk()
root.title("Speech Recognition and Response")

# Load the doctor image from local file system
image_path = "download.jpg"  # Update with the correct path
img = Image.open(image_path)
img = img.resize((200, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Create an image label
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create the status label
status_label = tk.Label(root, text="Click the button and speak")
status_label.pack()

# Create the conversation text area
conversation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
conversation_text.pack()

# Create the recognize button
recognize_button = tk.Button(root, text="Talk now", command=recognize_speech)
recognize_button.pack()

# Run the main event loop
root.mainloop()