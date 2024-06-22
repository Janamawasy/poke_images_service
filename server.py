import uvicorn
from fastapi import FastAPI, HTTPException, Request
from DAL.mongodb_api import MongoAPI

# data = {
#     "database": "poke_images",
# }

app = FastAPI()

@app.get('/')
async def get_image(poke_name: str):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.get_image_data(poke_name)
        if not response:
            raise HTTPException(status_code=404, detail='Pokemon does not exist')
        return response
    except HTTPException as e:
        print(e)

@app.get('/all_images')
async def get_all_images():
    return "all images here"


@app.post('/')
async def add_image(poke_name):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.add_image(poke_name)
        if isinstance(response, str):
            raise HTTPException(status_code=404, detail=response)
        return {"detail": "Image added successfully"}
    except HTTPException as e:
        print(e)

@app.put('/')
async def update_image(poke_name, new_image_url):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.replace_image(poke_name, new_image_url)
        if not response:
            raise HTTPException(status_code=404, detail=f"{poke_name} image do not exist in mongodb!")
        return {"detail": f"{poke_name} Image updated successfully"}
    except HTTPException as e:
        print(e)

@app.delete('/')
async def delete_image(poke_name):
    try:
        poke_interactor = MongoAPI()
        response = poke_interactor.delete_image(poke_name)
        if not response:
            raise HTTPException(status_code=404, detail=f"{poke_name} do not exist in db, double check pokemon name!")
        return {"detail": f"{poke_name} Image Deleted successfully"}
    except HTTPException as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)