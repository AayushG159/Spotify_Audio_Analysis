import requests
import json
from bs4 import BeautifulSoup

year_start, year_end = 2010, 2023

billboard_data = {}

for year in range(year_start, year_end + 1):

    # Send a GET request to the Wikipedia page
    response = requests.get(f'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}')

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the class 'wikitable'
    table = soup.find('table', {'class': 'wikitable'})

    # Initialize lists to store song names and artists
    ranks = []
    song_names = []
    artists = []

    # Find all rows in the table
    rows = table.find_all('tr')

    # Iterate through each row, skipping the header row
    for row in rows[1:]:
        # Find the cells in the row
        cells = row.find_all('td')
        
        # Extract the song name and artist from the cells
        rank = cells[0].text.strip()
        song_name = cells[1].text.strip()
        if len(cells) > 2:
            artist = cells[2].text.strip()
        else:
            artist = artists[-1]
        
        # Append the song name and artist to their respective lists
        ranks.append(rank)
        song_names.append(song_name)
        artists.append(artist)

    # Create a dictionary with song names and artists
    billboard_data[year] = [{'rank': rank, 'name': name, 'artist': artist} for rank, name, artist in zip(ranks, song_names, artists)]
    
    print(f'{year} year completed ')    

# Save the data as a JSON file
with open('billboard_data.json', 'w') as json_file:
    json.dump(billboard_data, json_file, indent=4)

print("JSON file 'billboard_data.json' created successfully.")