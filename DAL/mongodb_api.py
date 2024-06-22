import json
import os
from gridfs import GridFS
from pymongo import MongoClient
from utils import get_pokemon_image, store_image_in_mongo, store_image_in_folder, get_pokemon_id, retrieve_image_data_by_poke_name, save_image
from dotenv import load_dotenv

load_dotenv()


def update_config():
    try:
        config = {'created_db': 1}
        # Write the updated configuration back to the file
        with open('config.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except Exception as e:
        print(e)


def open_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        return config['created_db']
    except Exception as e:
        print(e)


class MongoAPI:
    def __init__(self):
        self.host = os.getenv('MONGO_DB_HOST')
        self.port = os.getenv('MONGO_DB_PORT')
        self.db_name = os.getenv('MONGO_DB_NAME')
        self.client = MongoClient(f'mongodb://{self.host}:{self.port}/')
        self.db = self.client[self.db_name]
        self.fs = GridFS(self.db)
        if open_config() == 0:
            if self.initialize_database():
                update_config()

    def initialize_database(self) -> bool:
        try:
            with open('data/pokemons_data.json', 'r') as file:
                data = json.load(file)
            print("initializing database started, it will take few minutes, please wait")
            for entry in data:
                image_url = get_pokemon_image(entry['name'])
                store_image_in_folder(image_url, entry['id'])
                store_image_in_mongo(self.fs, entry['id'], entry['name'])
            print("initializing database finished")
            return True
        except Exception as e:
            print(f"Error in initializing database\n{e}")
            return False

    def add_image(self, poke_name):
        # check if image exist
        data = self.db['fs.files'].find_one({"filename": f"{poke_name}.svg"})
        if not data:
            # if not, add new image
            poke_id = get_pokemon_id(poke_name)
            image_url = get_pokemon_image(poke_name)
            if poke_id and image_url:
                store_image_in_folder(image_url, poke_id)
                store_image_in_mongo(self.fs, poke_id, poke_name)
                print(f"{poke_name} image added successfully")
                return True
            else:
                # print(f"{poke_name} pokemon name not valid")
                msg = f"{poke_name} pokemon name not valid"
                return msg
        else:
            # print(f"{poke_name} image already exist in mongodb!")
            msg = f"{poke_name} image already exist in mongodb!"
            return msg


    def replace_image(self, poke_name, new_image_url):
        # check if poke_name exist in db
        data = self.db['fs.files'].find_one({"filename": f"{poke_name}.svg"})
        if data:
            # if exist, replace image
            poke_id = get_pokemon_id(poke_name)
            store_image_in_folder(new_image_url, poke_id)
            store_image_in_mongo(self.fs, poke_id, poke_name)
            return True
        else:
            return False

    def get_image_data(self, poke_name):
        image_data = retrieve_image_data_by_poke_name(self.db, self.fs, poke_name)
        if image_data:
            print(f"{poke_name} image data retrieved successfully")
            return image_data
        else:
            print(f"{poke_name} image data not found, double check pokemon name!")

    def show_image(self, poke_name):
        try:
            image_data = self.get_image_data(poke_name)
            if image_data:
                save_image(image_data)
                print(f"{poke_name} image saved in image.svg")
        except Exception as e:
            print(f"Error in saving image data. \n{e}")

    def delete_image(self, poke_name):
        try:
            data = self.db['fs.files'].find_one({"filename": f"{poke_name}.svg"})
            if data:
                poke_id = data['_id']
                print(poke_id)
                self.db['fs.files'].delete_one({"filename": f"{poke_name}.svg"})
                self.db['fs.chunks'].delete_one({"files_id": poke_id})
                return True
            else:
                return False
        except Exception as e:
            print(f"Error in deleting data. \n{e}")
