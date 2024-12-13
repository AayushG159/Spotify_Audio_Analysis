# Spotify_Audio_Analysis

A visual analytics system that enables users to understand what really makes a song popular through audio analysis. It supports high-level and low-level audio feature analysis. This repo mainly consists of Python scripts used to fetch and create our dataset, as there is no readily available dataset. Billboard Year-End Charts Top 100 songs from 2010 to 2023 are used to determine the most popular songs on a year-on-year basis. This repo mainly consists of scripts that were used for dataset creation. Another [repo](https://github.com/AayushG159/spotify-aa-ui) has the related visual analytics system that uses this data.

## Scripts
- `billboard_charts.py` - Scrapes Billboard charts year-on-year from Wikipedia
- `spotify_api_data.py` - Main script that fetches data using Spotify API and scraped charts
    - `get_spotify_tracks_from_playlist()` - Uses Get Playlist Items API to get individual track IDs from playlists (that were manually searched/created)
    - `get_spotify_audio_features()` - Uses Get Audio Features API (deprecated - November 27, 2024) to get high-level audio features for each track using track ID

## Data
- `billboard_data.json` - Scraped Data from Wikipedia that contains Billboard Year-End Top 100 Charts
- `spotify_playlists.json` - Manually curated playlist URLs that correspond to Billboard charts
- `spotify_track_ids.json` - Track IDs from playlists using `get_spotify_tracks_from_playlist()`
- `track_features.json` - Audio features for each track using `get_spotify_audio_features()`

## Installation

1. Clone the repository
2. Create a virtual environment using `python -m venv venv`
3. Install packages using `pip install -r requirements.txt`

## Using Spotify API

1. Create a web app in spotify dashboard. They have the necessary instructions on how to do so. 
2. Create the following file `env/secrets.py`
``` py
class Spotify:    
    CLIENT_ID = '<client_id>'
    CLIENT_SECRET = '<client_secret>'
    ACCESS_TOKEN = '<access_token>'
```
3. Run `generate_access_token()` in `spotify_api_data.py` to get the access token once `CLIENT_ID` and `CLIENT_SECRET` are filled in
