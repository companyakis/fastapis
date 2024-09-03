# areas.py file

from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint")
async def first_msg():
    return {"message": "Hi there!"}
