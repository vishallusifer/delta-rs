from sqlmodel import Field, SQLModel, create_engine, Relationship

class Airports_Info(SQLModel, table=True):
    id: int = Field(primary_key=True)
    code: str = Field(primary_key=True)
    name: str

class Flights_Schedule(SQLModel, table=True):
    id: int = Field(primary_key=True)
    created_at: str
    updated_at: str
    flight_identifier: str
    flt_num: str
    scheduled_origin_gate: str
    scheduled_destination_gate: str
    out_gmt: str
    in_gmt: str
    off_gmt: str
    on_gmt: str
    destination: str
    origin: str
    destination_full_name: str
    origin_full_name: str
    flights_schedulecol: str