from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated


app = FastAPI()

class Zepto(SQLModel, table=True):

    category: str = Field(index=True, primary_key=True)
    name: str = Field(index=True)
    mrp:float = Field(index=True)
    discount_percent:int = Field(index=True)
    available_quantity: int = Field(index=True)
    discounted_selling_price: float = Field(index=True)
    weight_in_gms:int = Field(index=True)
    out_of_stock:bool = Field(index=True)
    quantity:int = Field(index=True)

class ZeptoPut(SQLModel):

        category: str | None = None
        name: str | None = None
        mrp: float | None = None
        discount_percent: int | None = None
        available_quantity: int | None = None
        discounted_selling_price: float | None = None
        weight_in_gms: int | None = None
        out_of_stock: bool | None = None
        quantity: int | None = None


sqlite_url = "postgresql://postgres:12345@localhost:5432/sales_data"
engine = create_engine(sqlite_url, echo=False)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.post("/zepto/add")
async def add_zepto(zepto: Zepto,session: SessionDep) -> Zepto:
    session.add(zepto)
    session.commit()
    session.refresh(zepto)
    return zepto


@app.get("/zepto/{category}")
async def get_zepto(category: str, session: SessionDep):
    z = session.get(Zepto,category)
    if not z:
        raise HTTPException(status_code=404, detail="zepto not found")
    return z

@app.get("/zepto/")
async def get_zepto(session: SessionDep):
    result = session.exec(select(Zepto)).all()

    # Fetch all results from the executed statement

    if not result:
        raise HTTPException(status_code=404, detail="zepto not found")
    return result

@app.delete("/zepto/delete/{category}")
async def delete_zepto(session: SessionDep, category:str):
    zepto = session.get(Zepto, category)
    session.delete(zepto)
    session.commit()
    return zepto

@app.put("/zepto/update/{category}" ,response_model=Zepto)

async def update_zepto(category:str, zepto: ZeptoPut, session: SessionDep):
    zepto_put = session.get(Zepto, category)
    if not zepto_put:
        raise HTTPException(status_code=404, detail="zepto not found")
    zepto_data = zepto.model_dump(exclude_unset=True)
    zepto_put.sqlmodel_update(zepto_data)
    session.add(zepto_put)
    session.commit()
    session.refresh(zepto_put)
    return zepto_put








