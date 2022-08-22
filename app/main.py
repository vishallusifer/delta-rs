from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.flight_search import flight_search_router
from .api.airport_list import airport_list_router


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flight_search_router)
app.include_router(airport_list_router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Delta Assessment"}