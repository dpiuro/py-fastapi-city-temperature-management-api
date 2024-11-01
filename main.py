from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TemperatureData(BaseModel):
    city: str
    temperature: float

# Словник для зберігання температури для міст
temperature_db = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the City Temperature Management API"}

@app.get("/temperature/{city}")
def get_temperature(city: str):
    temperature = temperature_db.get(city)
    if temperature is not None:
        return {"city": city, "temperature": temperature}
    return {"city": city, "temperature": "Data not available"}

@app.post("/temperature/")
def set_temperature(data: TemperatureData):
    temperature_db[data.city] = data.temperature
    return {"message": f"Temperature for {data.city} set to {data.temperature}°C"}
