from fastapi import FastAPI

# The FastAPI class is going to provide all the things that we need
# for the correct function of our API
# Create an instance for this class
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET with a parameter without a type
@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# GET with a parameter with a type
@app.get("/second_item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

"""When you need to use two similar URLS 
one option it's to put in the first place
the url that you need yo execute firts, 
however a better way to do this is to import
Enum"""
from enum import Enum


class NumberStringModel(str, Enum):
    one_call = 'One'
    two_call = 'Two'
    three_Call = 'Three'


@app.get("/models/{model_name}")
async def get_model(model_name: NumberStringModel):
    # there are two ways to call something inside the model
    if model_name == NumberStringModel.one_call:
        return {"model_name": model_name,
                "message": "Calling the first element"}
    elif model_name.value == 'Two':
        return {"model_name": model_name,
                "message": "Calling the second element"}
    return {"model_name": model_name,
                "message": "Calling the last element"}


'''This new example is very
similar to the last model, but 
this uses int values not str in
the url'''
class NumberModel(int, Enum):
    one_call = 1
    two_call = 2
    three_Call = 3


@app.get("/number_models/{model_number}")
async def get_model(model_number: int = NumberModel):
    # there are two ways to call something inside the model
    if model_number == NumberModel.one_call:
        return {"model_name": model_number,
                "message": "Number 1"}
    elif model_number.__int__() == 2:
        return {"model_name": model_number,
                "message": "Number 2"}
    return {"model_name": model_number,
                "message": "Number 3"}


if __name__ == '__main__':
        print('Is working')

# Remember run this command in your terminal
# Uvicorn main:my_awesome_api --reload