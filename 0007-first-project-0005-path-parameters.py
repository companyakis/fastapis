from fastapi import FastAPI

app = FastAPI()

CITIES = [
    {"name": "Ankara", "mayor": "Mansur Yavaş", "country": "Turkiye"},
    {"name": "Istanbul", "mayor": "Ekrem İmamoğlu", "country": "Turkiye"},
    {"name": "Izmir", "mayor": "Cemil Tugay", "country": "Turkiye"},
    {"name": "Adana", "mayor": "Zeydan Karalar", "country": "Turkiye"},
]

@app.get("/cities")
async def city_info():
        return CITIES
    
@app.get("/cities/{city_title}")
async def returning_city(city_title: str):
    for c in CITIES:
        if c.get("name").casefold() == city_title.casefold():
            return c
