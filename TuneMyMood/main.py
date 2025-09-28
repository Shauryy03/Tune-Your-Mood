# main.py

import cv2
import streamlit as st
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-public"
))

# Mood mapping to Spotify keywords
mood_songs = {
    'happy': 'happy upbeat',
    'sad': 'sad mellow',
    'angry': 'rock aggressive',
    'surprise': 'pop energetic',
    'fear': 'calm relaxing',
    'neutral': 'chill soft'
}

# Function to detect mood using DeepFace
def detect_emotion():
    cap = cv2.VideoCapture(0)
    emotion = 'neutral'

    ret, frame = cap.read()
    if ret:
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            # DeepFace may return a list or dict depending on version
            if isinstance(result, list):
                emotion = result[0]['dominant_emotion']
            else:
                emotion = result['dominant_emotion']
        except Exception as e:
            print("Emotion detection failed:", e)
            emotion = 'neutral'

    cap.release()
    cv2.destroyAllWindows()
    return emotion

# Function to get songs by mood
def get_songs_by_mood(mood):
    query = mood_songs.get(mood, 'pop')
    results = sp.search(q=query, limit=10, type='track')
    return [track['uri'] for track in results['tracks']['items']]

# Function to create Spotify playlist
def create_playlist(user_id, mood, track_uris):
    playlist = sp.user_playlist_create(user_id, name=f"ModeChange - {mood.capitalize()} Mood", public=True)
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    return playlist['external_urls']['spotify']

# Streamlit UI
st.title("🎵 TuneMyMood – Mood-Based Music Recommender")

if st.button("Detect My Mood & Generate Playlist"):
    st.write("Detecting your mood...")
    mood = detect_emotion()
    st.write(f"Your current mood is **{mood.capitalize()}**")

    user_id = sp.current_user()['id']
    track_uris = get_songs_by_mood(mood)
    playlist_url = create_playlist(user_id, mood, track_uris)

    st.success("Playlist created successfully!")
    st.markdown(f"[Open Playlist in Spotify]({playlist_url})")
