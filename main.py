from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated


app = FastAPI()

class zepto(SQLModel, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    category: str = Field(index=True, primary_key=True)
    name: str = Field(index=True)
    mrp:float = Field(index=True)
    discount_percent:int = Field(index=True)
    available_quantity: int = Field(index=True)
    discounted_selling_price: float = Field(index=True)
    weight_in_gms:int = Field(index=True)
    out_of_stock:bool = Field(index=True)
    quantity:int = Field(index=True)


sqlite_url = "postgresql://postgres:12345@localhost:5432/sales_data"
engine = create_engine(sqlite_url, echo=False)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/zepto/{category}")
async def get_zepto(category: str, session: SessionDep):
    z = session.get(zepto,category)
    if not z:
        raise HTTPException(status_code=404, detail="Hero not found")
    return z




