# routers/heroes.py
from fastapi import APIRouter, Depends
from typing import List
from models.hero import Hero, get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/heroes", response_model=List[Hero])
async def get_heroes(db: Session = Depends(get_db)):
    return db.query(Hero).all()

@router.get("/heroes/{hero_id}", response_model=Hero)
async def get_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.query(Hero).get(hero_id)
    return hero

@router.post("/heroes", response_model=Hero)
async def create_hero(hero: Hero, db: Session = Depends(get_db)):
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero