from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# نموذج للطلب (Request Body)
class Numbers(BaseModel):
    number1: float
    number2: float

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI server 🎉"}

@app.get("/add")
def add(number1: float, number2: float):
    result = number1 + number2
    return {"operation": "addition", "result": result}

@app.post("/multiply")
def multiply(data: Numbers):
    result = data.number1 * data.number2
    return {"operation": "multiplication", "result": result}



