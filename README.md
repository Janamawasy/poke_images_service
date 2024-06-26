# Pokemon Project

This service is part of a microservice architecture project. It acts as a FastAPI server that interacts with a MongoDB database and the Pokemon API to store and manage Pokemon images data. The images are stored in SVG format using GridFS.

## Gateway Project
For more details on the entire microservice architecture, refer to :
[gateway project](https://github.com/Janamawasy/getaway-poke-service/tree/master).

## Features

- Retrieve a Pokemon image by Pokemon name
- Add a new Pokemon image
- Delete an existing Pokemon image
- Update an existing Pokemon image
- Display a Pokemon image

## Technologies Used

- Python
- FastAPI
- MongoDB
- pymongo
- Requests
- GridFS


## Running the Application in Docker
1. Initialize the database**: To migrate data from `data/pokemons_data.json` to MongoDB, ensure `config.json` is set to:
   ```
   {
    "created_db": 0
   }
   ```
2. Set up environment: Ensure .env contains:
   ```
      MONGO_DB_HOST = mymongo
   ```

1. Start the FastAPI server:
    ```sh
      docker-compose up
    ```


## Running the Application Locally
1. Initialize the database: To migrate data from data/pokemons_data.json to MongoDB, ensure config.json is set to:   ```
   ```
   {
    "created_db": 0
   }
   ```
  - if the database already stored in Mongo db, no need to reset 'data/pokemons_data.json', it should be:
  ```
   {
    "created_db": 0
   }
   ```
2. Set up environment: Ensure .env contains:
   ```
      MONGO_DB_HOST = localhost
   ```

1. Start the FastAPI server:
    ```sh
      uvicorn server:app --reload --port 8002
    ```

## Testing

1. To run the tests:
    ```
      tests/images_tests.py
    ```

