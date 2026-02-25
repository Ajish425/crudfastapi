from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
@app.post("/submit", response_class=HTMLResponse)
async def meta_data( request: Request,nm: str = Form(...)):

    data ={"request": request,"name":nm}
    return templates.TemplateResponse("item.html",data)



