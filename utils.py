from fastapi import requests
import os
import requests

def get_pokemon_image(pokemon_name):
    try:
        pokemon_api_url = "https://pokeapi.co/api/v2/pokemon"
        response = requests.get(f'{pokemon_api_url}/{pokemon_name.lower()}')
        if response.status_code == 200:
            data = response.json()
            image = data['sprites']['other']['dream_world']['front_default']
            return image
    except IOError:
        return False

def get_pokemon_id(pokemon_name):
    try:
        pokemon_api_url = "https://pokeapi.co/api/v2/pokemon"
        response = requests.get(f'{pokemon_api_url}/{pokemon_name.lower()}')
        if response.status_code == 200:
            data = response.json()
            id = data['id']
            return id
    except IOError:
        return False

def store_image_in_folder(image_url, image_id):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            svg_path = os.path.join('images/', f'poke_{image_id}.svg')
            with open(svg_path, 'wb') as f:
                f.write(response.content)
            return True
    except IOError:
        return False


def store_image_in_mongo(fs, poke_id, poke_name):
    try:
        with open(f'images/poke_{poke_id}.svg', 'rb') as f:
            contents = f.read()
        if fs.put(contents, filename=f"{poke_name}.svg"):
            return True
    except IOError:
        return False


def retrieve_image_data_by_poke_name(db, fs, poke_name):
    try:
        data = db['fs.files'].find_one({"filename": f"{poke_name}.svg"})
        if data:
            fs_id = data['_id']
            image_data = fs.get(fs_id).read()
            return image_data
    except IOError:
        return False



def save_image(data):
    try:
        with open("image.svg", 'wb') as f:
            f.write(data)
        return True
    except IOError:
        return False


# example_svg = b'<?xml version=\'1.0\' encoding=\'utf-8\'?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="183px" height="219px" viewBox="-0.45 -0.4 183.1 218.7"><path fill="#a3611c" d="M126.45 62.05 Q135.15 71.8 139.75 84.2 144.45 97.0 144.0 110.5 143.0 139.1 125.55 156.65 109.0 173.35 85.0 173.35 58.6 173.35 39.7 155.95 20.2 138.1 19.25 111.15 18.75 97.95 22.95 85.3 27.15 72.75 35.25 62.85 53.2 41.0 80.85 41.0 94.1 41.0 106.1 46.7 117.65 52.15 126.45 62.05"/><path fill="#a3611c" d="M29.4 144.3 Q23.7 152.1 12.7 153.5 L5.25 153.3 Q2.15 152.6 1.95 151.2 1.6 148.55 8.85 138.65 16.3 128.5 21.3 125.4 21.85 131.3 29.4 144.3"/><path fill="#fdebd1" d="M51.05 118.9 Q60.05 115.25 70.7 115.25 86.2 115.25 99.55 119.75 112.25 124.1 119.65 131.35 127.15 138.8 126.8 147.1 126.45 156.05 116.9 163.95 110.05 167.85 105.3 169.7 L110.55 177.65 98.05 173.15 96.2 181.0 85.25 174.8 79.1 182.4 74.7 174.15 61.05 179.6 62.9 172.7 53.3 174.75 52.4 174.5 Q52.25 174.1 52.65 173.55 L56.95 167.6 Q49.7 164.3 38.5 155.1 32.65 148.5 32.6 141.2 32.55 134.4 37.6 128.35 42.55 122.4 51.05 118.9"/><path fill="#c18963" d="M79.1 182.4 L85.45 174.5 92.55 178.75 Q92.4 185.75 92.75 187.35 92.95 188.3 94.6 189.3 L97.85 190.95 Q101.4 192.8 109.9 193.25 112.5 193.4 114.5 197.6 116.65 202.1 114.45 205.55 112.65 208.4 109.9 209.0 107.4 209.55 104.7 208.15 104.0 213.5 93.85 213.05 92.4 213.0 90.45 211.15 L88.75 209.35 Q82.7 208.45 77.2 209.25 75.9 210.95 72.75 212.05 69.1 213.3 65.75 212.5 62.05 211.65 60.8 210.2 59.45 208.75 60.45 206.5 50.95 206.5 50.9 201.1 50.85 197.6 52.95 194.45 55.35 190.9 58.9 190.9 L64.95 190.9 69.5 190.4 Q71.2 189.85 72.7 188.7 74.05 187.6 74.2 186.85 L74.6 180.85 74.8 174.65 79.1 182.4"/><path fill="#ffffff" d="M59.3 204.55 L54.5 207.35 Q49.85 210.0 49.15 209.5 48.05 208.8 49.55 204.55 51.15 199.95 54.1 198.25 56.1 199.45 57.6 201.1 59.35 203.05 59.3 204.55"/><path fill="#ffffff" d="M71.0 208.4 Q71.9 210.65 67.35 214.3 62.85 217.85 62.3 217.25 60.65 215.6 61.25 210.85 61.85 206.2 63.5 205.35 66.0 204.1 68.5 205.7 70.35 206.9 71.0 208.4"/><path fill="#ffffff" d="M94.15 209.55 Q93.8 206.55 96.9 205.25 100.0 203.95 101.75 206.15 102.45 207.05 102.2 209.6 101.95 211.9 101.1 214.1 100.1 216.85 99.25 216.9 98.6 217.0 97.5 215.35 L95.6 212.45 Q94.25 210.25 94.15 209.55"/><path fill="#ffffff" d="M111.3 206.15 Q110.4 204.65 111.15 202.3 111.9 199.85 113.7 199.4 115.5 198.95 117.9 202.2 120.1 205.15 120.85 208.2 121.3 209.95 120.8 210.35 120.3

#### tests
# Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['poke_images']
# fs = GridFS(db)

# store_image_in_folder('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png', 10)
# store_image_in_mongo(fs, 10, "pikachu")
# retrieve_image_data_by_name(fs, "pikachu")

# image_url = get_pokemon_image("pikachu")
# print('image_url', image_url)
# store_image_in_folder(image_url, 1000001)
# store_image_in_mongo(fs, 1000001, "pikachu")
# retrieve_image_by_poke_name(db, "pikachu", 'mm')
# image_data = retrieve_image_data_by_poke_name(db, fs, "hoothoot")
# save_image(image_data)

