import os
import json
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import cast, String
from models import MenuItem, Base
from schemas import MenuItemSchema
from databases import get_db, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MENU_PATH = os.path.join(BASE_DIR, "menu_data.json")
WEB_DIR = os.path.join(BASE_DIR, "web")

with open(MENU_PATH, "r", encoding="utf-8") as f:
  menu_data = json.load(f)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = next(get_db())
    for item in menu_data:
        exists = db.query(MenuItem).filter(
            cast(MenuItem.name['en'].astext, String) == item['name']['en']
        ).first()
        if not exists:
            menu_item = MenuItem(
                name=item['name'],
                description=item.get('description', {}),
                weight=item.get('weight', {}),
                price=item['price'],
                image=item.get('image', '')
            )
            db.add(menu_item)
    db.commit()
    db.close()
    yield
  
app = FastAPI(lifespan=lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.mount("/web", StaticFiles(directory=WEB_DIR, html=True), name="web")

@app.get("/menu", response_model=list[MenuItemSchema])
def get_menu(db: Session = Depends(get_db)):
  items = db.query(MenuItem).all()
  return items
