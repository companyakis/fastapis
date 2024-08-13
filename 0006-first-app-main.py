from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
async def home():
    return {"first message": "Hi there!"}

# let's add a second func

@app.get("/blog/aboutme")
async def myblog():
    return {"about me": "Mustafa Buyukdereli"}


# terminal code => fastapi dev main.py
