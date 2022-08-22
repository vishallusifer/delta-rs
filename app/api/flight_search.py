from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional
from app.db import engine
from app.models import Flights_Schedule


flight_search_router = APIRouter()

@flight_search_router.get("/searchFlight/")
def searchFlight(flight):
  resp = []
  airport_to_search = flight
  airport_to_search = (airport_to_search.split(':')[0]).strip()
  with Session(engine) as session:
    statementOrigin = select(Flights_Schedule).where(Flights_Schedule.origin == airport_to_search)
    statementDest = select(Flights_Schedule).where(Flights_Schedule.destination == airport_to_search)
    statementOriginName = select(Flights_Schedule).where(Flights_Schedule.origin_full_name == airport_to_search)
    statementDestName = select(Flights_Schedule).where(Flights_Schedule.destination_full_name == airport_to_search)
    resp.extend(session.exec(statementOrigin).all())
    resp.extend(session.exec(statementDest).all())
    resp.extend(session.exec(statementOriginName).all())
    resp.extend(session.exec(statementDestName).all())    
  return resp


