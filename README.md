🗣️ Doctor Voice Assistant Bot (Gemini + Speech Recognition)
A desktop-based voice-enabled AI assistant that simulates a soft-spoken doctor interacting with patients. Built using Google Gemini (Generative AI), real-time speech recognition, and text-to-speech synthesis—all inside a simple Python GUI.

🧠 Features
🎙️ Speech Recognition via speech_recognition (Google Speech API).

💬 Conversational AI using Gemini 1.5 Flash (google.generativeai).

🔊 Voice Output using pyttsx3 (offline TTS engine).

🧑‍⚕️ Doctor Persona: Bot responds gently, as a virtual medical expert.

🖼️ Tkinter GUI: Clean UI with doctor image, conversation log, and one-click interaction.

⚡ Multithreaded Speech Listener: No freezing while listening or processing speech.

📦 Tech Stack
Language: Python

Frontend: Tkinter (GUI), PIL (Image handling)

Voice Input: speech_recognition + Google Speech API

GenAI: Google Gemini 1.5 Flash

Voice Output: pyttsx3 (TTS engine)

Threading: threading.Thread for async audio handling

📷 UI Preview
Displays a doctor image

Shows conversation text history (you and bot)

One button to activate listening mode

🚀 How It Works
Click "Talk now"

Speak your question (e.g., “I have a headache, what should I do?”)

Gemini processes your query in the context of a doctor's tone.

The bot speaks the answer aloud and displays it in the GUI.

🛠️ Setup Instructions
Install dependencies
pip install google-generativeai speechrecognition pyttsx3 Pillow
Set up your Google Gemini API key

genai.configure(api_key="YOUR_API_KEY")

Run the script
python your_script.py
🔐 Note: Make sure your microphone is accessible and internet is connected for Gemini and Google Speech API to work.

