# 🎵 Moodify – Emotion-Based Music Recommender

Moodify is an AI-powered project that detects your **facial expressions in real-time** using **DeepFace** and automatically generates a **Spotify playlist** that matches your mood.  
It combines **Deep Learning (DeepFace)** with **Spotify API** to bring music recommendations that adapt to your emotions instantly.

---

## ✨ Features
- 🎭 **Real-time Emotion Detection** using your webcam (happy, sad, angry, neutral, etc.)
- 🎶 **Spotify Playlist Generation** based on detected mood
- 🤝 **Integration with Spotify API** for personalized music
- 📷 **DeepFace-based Facial Emotion Recognition** for accurate mood detection
- 🌐 **Streamlit Web App** for easy and interactive use

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit** – Web interface
- **OpenCV** – Webcam access
- **DeepFace** – Emotion detection
- **Spotipy** – Spotify API integration
- **Spotify Developer API** – For playlist creation

---

## 📂 Install dependencies
    pip install streamlit
    pip install opencv-python
    pip install deepface
    pip install spotipy
    pip install pandas
    pip install tensorflow

---

## 📂 Setup Spotify Developer API
     Go to Spotify Developer Dashboard : https://developer.spotify.com/dashboard/
     Create a new app → Get Client ID and Client Secret.
     Set Redirect URI to : http://127.0.0.1:8501/
    Create a file spotify_config.py inside your project and add:
           CLIENT_ID = "your_client_id"
           CLIENT_SECRET = "your_client_secret"
           REDIRECT_URI = "http://localhost:8501/callback"
           
---

## Run Project
       streamlit run main.py




