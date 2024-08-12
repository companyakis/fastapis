from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"my_first_msg" : "Hi there!"}

@app.get("/home")
def index2():
    return {"my_second_msg" : "Hi again!"}

@app.get("/blog/aboutme")
def index3():
    return {"about me" : "My name is Mustafa Buyukdereli"}

# uvicorn main:app --reload
