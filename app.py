import streamlit as st
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API 
CLIENT_ID = "f34e5870f9e24bb289badaac41898f30"
CLIENT_SECRET = "a4a0f376996d433b896660a2e4ff7b6a"

# Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to fetch album and link
def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        song_url = track["external_urls"]["spotify"]  # Spotify link
        return album_cover_url, song_url
    else:
        # image and link
        return "https://i.postimg.cc/0QNxYz4V/social.png", "#"

# Function to recommend songs
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_info = []
    
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        poster_url, song_url = get_song_info(song_name, artist)
        recommended_music_info.append((song_name, poster_url, song_url))

    return recommended_music_info

# Streamlit UI
st.set_page_config(page_title="Music Recommender System", page_icon="🎵", layout="wide")
st.markdown('<div class="custom-header">🎵 Music Recommender System 🎵</div>', unsafe_allow_html=True)
st.subheader("Find music you’ll love, tailored just for you!")

# Load data
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_song = st.selectbox("Type or select a song from the dropdown", music_list)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_song)
    cols = st.columns(5)

    for i, (col, (song_name, poster_url, song_url)) in enumerate(zip(cols, recommendations)):
        with col:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <a href="{song_url}" target="_blank">
                        <img src="{poster_url}" alt="{song_name}" style="width: 100%; border-radius: 10px;">
                    </a>
                    <p style="color: white; font-size: 14px; margin-top: 10px;">{song_name}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
