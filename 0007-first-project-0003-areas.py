from fastapi import FastAPI

app = FastAPI()

CITIES = [
    {"name": "Ankara", "mayor": "Mansur Yavaş", "country": "Turkiye"},
    {"name": "İstanbul", "mayor": "Ekrem İmamoğlu", "country": "Turkiye"},
    {"name": "İzmir", "mayor": "Cemil Tugay", "country": "Turkiye"},
    {"name": "Adana", "mayor": "Zeydan Karalar", "country": "Turkiye"},
]


@app.get("/endpoint")
async def first_msg():
    return {"message": "Hi there!"}

@app.get("/all-cities")
async def ciyy_info():
        return CITIES
