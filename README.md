# Spotify_Audio_Analysis

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