from fastapi import FastAPI

app = FastAPI()

AREAS = [
    {"title": "AI", "main_lang": "Python"},
    {"title": "Web3", "main_lang": "Rust"},
]


@app.get("/endpoint")
async def first_msg():
    return {"message": "Hi there!"}

@app.get("/areas")
async def all_areas():
        return AREAS
