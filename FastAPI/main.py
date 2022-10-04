from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Welcome to the world of FastAPI!"}


@app.get('/items/{item}')
def get_items(item, qunatity=None):
    return {"item": item, "qunatity": qunatity}
