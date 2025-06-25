# 🗣️ Doctor Voice Assistant Bot (Gemini + Speech Recognition)

A desktop-based **voice-enabled AI assistant** that simulates a soft-spoken doctor interacting with patients. Built using **Google Gemini (Generative AI)**, real-time **speech recognition**, and **text-to-speech synthesis** — all inside a simple Python GUI.

---

## 🧠 Features

- 🎙️ **Speech Recognition** via `speech_recognition` (Google Speech API)
- 💬 **Conversational AI** using Gemini 1.5 Flash (`google.generativeai`)
- 🔊 **Voice Output** using `pyttsx3` (offline TTS engine)
- 🧑‍⚕️ **Doctor Persona**: Bot replies softly like a medical professional
- 🖼️ **Tkinter GUI**: Clean UI with doctor image, chat log, and talk button
- ⚡ **Multithreaded Speech Listener**: No freezing during audio capture

---

## 📦 Tech Stack

- **Language**: Python  
- **Frontend**: Tkinter (GUI), PIL (Image handling)  
- **Voice Input**: `speech_recognition` + Google Speech API  
- **GenAI**: Google Gemini 1.5 Flash  
- **Voice Output**: `pyttsx3`  
- **Threading**: `threading.Thread` for async recognition  

---

## 📷 UI Preview

- 👨‍⚕️ Doctor image display  
- 💬 Real-time conversation history (User ↔️ Bot)  
- 🎛️ "Talk now" button to activate interaction  

---

## 🚀 How It Works

1. Click the **"Talk now"** button.
2. Speak your question (e.g., “I have a headache, what should I do?”).
3. Gemini processes your input and generates a soft, contextual response.
4. Bot speaks the response aloud and displays it in the text area.

---

## 🛠️ Setup Instructions

### 1. Install dependencies

```bash
pip install google-generativeai speechrecognition pyttsx3 Pillow

### 2. Set your Google Gemini API key

```bash
genai.configure(api_key="YOUR_API_KEY")

### 3. Run the bot

```bash
python your_script.py

