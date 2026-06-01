from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI()

items_db = {
    1: {"name": "Wireless Mouse", "price": 29.99},
    2: {"name": "Mechanical Keyboard", "price": 79.99}
}

class Item(BaseModel):
    name: str
    price: float


@app.get("/items")
def read_all_items():
    return items_db


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Item with ID {item_id} does not exist"
        )
    return items_db[item_id]


@app.post("/items")
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Item with ID {item_id} already exists"
        )
    items_db[item_id] = item.model_dump()
    return {"message": "Item successfully created", "data": items_db[item_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Item with ID {item_id} not found to update"
        )
    items_db[item_id] = item.model_dump()
    return {"message": "Item successfully updated", "data": items_db[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Item with ID {item_id} not found to delete"
        )
    del items_db[item_id]
    return {"message": f"Item {item_id} has been successfully deleted"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# question 1
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping/")
def ping():
    return {"status":"pong"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# question 2

from fastapi import FastAPI
import uvicorn

app = FastAPI()


data = {
    "1": {"user_id": 1, "name": "Alice", "email": "alice@gmail.com"},
    "2": {"user_id": 2, "name": "David", "email": "bob@gmail.com"},
}

@app.get("/")
def get_root():
    return  {"service": "my-api", "version": "1.0"}

@app.get("/users/admin")
def get_admin():
    return {"role": "admin", "access": "full"}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    return data.get(user_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# question 3

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/calc/{a}/{op}/{b}")
def calculate(a: int, op: str, b: int):
    operation = op.lower()
    valid_operations = ["add", "sub", "mul", "div"]
   
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        if b == 0:
            return {"error cannot divided bu zero"}
        result = a / b

    return {"operation": operation, "result": result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# question 4

from fastapi import FastAPI
import uvicorn
from datetime import datetime


app = FastAPI()

server_name = "production-omega-01"

@app.get("/status")
def get_system_status():
    current_time = datetime.now()

    return {"server_name": server_name, "timestamp": current_time}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



# question 5
from fastapi import FastAPI
import uvicorn



app = FastAPI()


grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

@app.get("/students")
def all_students():
    return {"students": grades}

@app.get("/students/top")
def highest_grade():
    return {max(value["grade"] for value in grades.values())}

@app.get("/students/average")
def class_average():
    average = 0
    for value in grades.values():
        average += value["grade"]
    return {average // len(grades)}

@app.get("/students/count")
def count_students():
    return {len(grades)}


@app.get("/students/{student_id} ")
def one_student(student_id:int):
    return grades.get(str(student_id))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
