import requests
import json

from env.secrets import Spotify

def generate_access_token(url: str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': Spotify.CLIENT_ID,
        'client_secret': Spotify.CLIENT_SECRET
    }
    response = requests.post(url=url, data=data, headers=headers)
    print(response.json())

def get_spotify_tracks_from_playlist(playlist_file: str):
    output = []
    with open(playlist_file, 'r') as file:
        file_data = json.load(file)
        for i in range(len(file_data)):
            year = int(file_data[i]['year'])
            playlist_url = file_data[i]['playlist']
            playlist_id = playlist_url.split('/')[-1]
            header = {
                'Authorization': f'Bearer {Spotify.ACCESS_TOKEN}'
            }
            url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
            print(f'Fetching Playlist Tracks for year {year} - ')
            response = requests.get(url=url, headers=header)
            response_data = response.json()
            if response.status_code == 200:
                print('Fetched. Processing...')
            else:
                print('Issue with fetching from API. Skipping')
                continue
            for ind, item in enumerate(response_data['items']):
                track = item['track']
                track_obj = {
                    "track_id": track['id'],
                    "name": track['name'],
                    "artists": [artist_obj['name'] for artist_obj in track['artists']],
                    "year": year,
                    "ranking": ind + 1
                }
                output.append(track_obj)
        with open('spotify_track_ids.json', 'w') as output_file:
            json.dump(output, output_file, indent=4)

def get_spotify_audio_features(tracks_file: str, output_file_path: str):
    output = []
    with open(tracks_file, 'r') as file:
        file_data = json.load(file)
        track_ids = [data['track_id'] for data in file_data]
        req_inputs = []
        ind = 0
        while ind < len(track_ids):
            req_inputs.append(','.join(track_ids[ind: ind+100]))
            ind += 100
        header = {
            'Authorization': f'Bearer {Spotify.ACCESS_TOKEN}'
        }
        for i, input in enumerate(req_inputs):
            print(f'Fetching Audio Features for year {2010+i} - ')
            url = f'https://api.spotify.com/v1/audio-features?ids={input}'
            response = requests.get(url=url, headers=header)
            response_data = response.json()
            if response.status_code == 200:
                print('Fetched. Processing...')
            else:
                print('Issue with fetching from API. Skipping')
                continue
            for j, item in enumerate(response_data['audio_features']):
                data_obj = file_data[100 * i + j]
                output.append({**data_obj, **item})
        with open(output_file_path, 'w') as output_file:
            json.dump(output, output_file, indent=4)       
                


if __name__ == '__main__':
    # token_url = 'https://accounts.spotify.com/api/token'
    # generate_access_token(token_url)
    # get_spotify_tracks_from_playlist(playlist_file='spotify_playlists.json')
    get_spotify_audio_features(tracks_file='./spotify_track_ids.json', output_file_path='track_features.json')