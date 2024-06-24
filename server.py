import io

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from DAL.mongodb_api import MongoAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get('/')
async def root():
    return 'dont miss the magic in localhost:8002/docs !'

@app.get('/data')
async def get_image(poke_name: str):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.get_image_data(poke_name)
        return response
    except HTTPException as e:
        raise e

@app.get('/image')
async def show_image(poke_name):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.get_image_data(poke_name)
        return StreamingResponse(io.BytesIO(response), media_type="image/svg+xml")
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/')
async def add_image(poke_name):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.add_image(poke_name)
        return response
    except HTTPException as e:
        raise e

@app.put('/')
async def update_image(poke_name, new_image_url):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.replace_image(poke_name, new_image_url)
        return response
    except HTTPException as e:
        raise e

@app.delete('/')
async def delete_image(poke_name):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.delete_image(poke_name)
        return response
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)