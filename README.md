## Music Recommender System

## Overview

The **Music Recommender System** is a web application that suggests personalized music based on your input. This system leverages Spotify’s extensive music library to recommend tracks similar to the one you choose. It provides an intuitive and interactive interface for users to discover new music tailored to their preferences.

## Features

- **Personalized Recommendations**: Get song suggestions based on your selected track.
- **Album Covers**: Display of album covers for each recommended song.
- **Direct Links to Spotify**: Click on any recommended song poster to be redirected to its Spotify page.
- **Interactive Interface**: A user-friendly web interface built with Streamlit.

## Requirements

To run this project locally, ensure you have the following:

- Python 3.6 or higher
- Streamlit
- Spotipy (for Spotify API interaction)
- Pandas
- Scikit-learn

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Install Dependencies

Use the following command to install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the libraries manually:

```bash
pip install streamlit spotipy pandas scikit-learn
```

### 3. Set Up Spotify API Credentials

Create an account and register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

Once you have your **Client ID** and **Client Secret**, add them to the code (or securely store them using environment variables).

```python
CLIENT_ID = "<your-client-id>"
CLIENT_SECRET = "<your-client-secret>"
```

### 4. Run the Application

Start the Streamlit app by running:

```bash
streamlit run app.py
```

This will open the app in your default browser, where you can interact with the music recommender system.

## How to Use

1. **Select a Song**: Use the dropdown to choose a song.
2. **Get Recommendations**: Click the "Show Recommendation" button to see music suggestions.
3. **Explore More**: Click on any of the album covers to open the song directly on Spotify.

## Technologies Used

- **Streamlit**: A fast and easy framework for creating web apps.
- **Spotipy**: A Python library for interacting with the Spotify API.
- **Pandas**: Used for data manipulation and storage.
- **Scikit-learn**: For calculating cosine similarity between songs based on their features.

## Future Improvements

- **Advanced Recommendation Algorithms**: Implementing machine learning models for better recommendations.
- **Song Preview**: Adding song previews in the app so users can listen before they visit Spotify.

## Acknowledgements

- **Spotify API**: For providing access to millions of songs and their metadata.
- **Streamlit**: For enabling rapid prototyping of web applications.
