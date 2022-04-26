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


#=============== QUERY PARAMETERS ==================

''' 
skip = it's the index where you're going to start
limit = the quantity of items to show you can modify the URL
http://127.0.0.1:8000/items/?skip=0&limit=1
you can modify the URL parameters the parameters
work as a common func in python, you can specify
only the first or maybe the second parameter 
as you want, and you can define some default
value if you want ...
'''
items = [
    {"first_item": "Foo"},
    {"second_item": "Bar"},
    {"third_item": "Baz"}
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 3): # Here u can see how we handle the data type
    return items[skip : skip + limit]


# As the same way you can declare optional parameters as the example below
from typing import Optional # It's necessary to import  this


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {
            "message": "Using the second argument 'q' ",
            "item_id": item_id, "q": q
        }
    return {
        "message": "You're not using the second argument",
        "item_id": item_id
    }

# Make a query parameter with Type conversion
'''
In this example you can use any of these urls and
the func is going to make a conversion of the type,
but the type should have some relation with the type
http://127.0.0.1:8000/items/foo?short=True
http://127.0.0.1:8000/items/foo?short=true
http://127.0.0.1:8000/items/foo?short=on
http://127.0.0.1:8000/items/foo?short=yes
IF YOU WANT TO DEFINE A PARAMETER AS REQUIRED ONLY
REMOVE THE OPTIONAL
'''
@app.get("/types/{simple_id}")
async def read_item(simple_id: str, q: Optional[str] = None, short: bool = False):
    item = {"simple_id": simple_id}
    if q:
        item.update({"q": q})
    elif not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item




if __name__ == '__main__':
    print('Is working')

# Remember run this command in your terminal
# Uvicorn main:app --reload
'''
http://127.0.0.1:8000/docs
in this URL you can see a friendly UI
to try your APIS
'''