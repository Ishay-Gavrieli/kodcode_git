import os
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

load_dotenv()
PORT = int(os.environ.get("PORT", 8000)) 


app = FastAPI(title="My To-Do List API")


todo_tasks = [
    {"id": 1, "task": "Set up project directory and venv", "completed": True},
    {"id": 2, "task": "Install requirements via pip", "completed": True},
    {"id": 3, "task": "Run the FastAPI server successfully", "completed": False}
]


@app.get("/")
def read_root():
    return {"status": "Success", "data": todo_tasks}


if __name__ == "__main__":
    print(f"Launching server on port {PORT}...")
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)


# question 

from fastapi import FastAPI
import uvicorn

app = FastAPI() 

@app.get("/") 
def read_root():
    return {"message": "Hello from my first API server this is sunday!",
            "my_name": "ishay"} 

# question 


from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# question 

from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get("/items/count")
def count_items():
    return {"count": 42, "description": "This is the total number of items."}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# question 

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}

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
