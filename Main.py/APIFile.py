from fastapi import FastAPI
num=FastAPI()
@num.get("/")
def weclome():
    return{"wecolme":"testing"}
@num.get("/equal")
def sum(number1:float , number2:int):
    return{number1 + number2}


