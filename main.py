from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello/")
async def create_item(product, id ):
    return {"message": product, "id": id}

@app.put("/product/{id}")
async def update_item(product, id):
    return {"message": product, "id": id}

@app.delete("/del/{id}")
async def delete_item(product, id):
    return {"message": product, "id": id}
