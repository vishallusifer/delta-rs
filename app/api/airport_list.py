from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from app.db import engine
from sqlmodel import Session, select
from app.models import Airports_Info




airport_list_router = APIRouter()

@airport_list_router.get("/airportDetails")
def getAirportDetails():
  resp = []
  with Session(engine) as session:
    statement = select(Airports_Info)
    results = session.exec(statement).all()
    for airport in results:
      resp.append(airport.code + " : " + airport.name)
    return resp


