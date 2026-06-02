# question 1
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1").json()

name = response["name"]
email = response["email"]
city = response["address"]["city"]

print(f"Name: {name}")
print(f"Email: {email}")
print(f"City: {city}") 


add1 = requests.get("https://jsonplaceholder.typicode.com/posts").json()

print(len(add1))


add2 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2").json()

for post in add2:
    print(post["title"])




# question 2
import requests

def safe_get(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    elif response.status_code == 404:
        return None
    
    else:
        raise Exception(f"error:request faild with status {response.status_code}")
    


# question 3
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
def greet_user(name:str):
    return {"message": f"Hello, {name}!"}



if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)



# question 4

import requests

posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = posts_response.json()

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
users = users_response.json()



user_dic = {}
for user in users:
        user_dic[user["id"]] = user["name"]

for post in posts:
    post_title = post["title"]
    author_id = post["userId"]

    author_name = user_dic.get(author_id)

    print(f"'{post_title}' by {author_name}")



# question 5

from fastapi import FastAPI
import uvicorn


app = FastAPI()


items = {"1":{"id":1,
        "description" :"",
        "name_item":"",
        "title":"",
        "complete":bool}
        }


@app.get("/items")
def all_items():
    return items.values()

@app.get("/items/{item_id}")
def get_item_by_id(item_id:int):
    if item_id not in items:
        return "error: the id not exists"
    return items[item_id]

@app.post("/items")
def create_item(title: str, description: str, name_item: str, complete: bool):
    new_id = max(items.keys(), default=0) + 1
    new_item = {
        "id": new_id,
        "title": title,
        "description": description,
        "name_item": name_item,
        "complete": complete
    }
    items[new_id] = new_item
    return new_item

@app.post("/items/category/{category_name}")
def create_item_in_category(category_name: str, title: str, description: str, complete: bool):
    new_id = max(items.keys(), default=0) + 1
    new_item = {
        "id": new_id,
        "title": title,
        "description": description,
        "name_item": category_name,
        "complete": complete
    }
    items[new_id] = new_item
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, title: str, description: str, name_item: str, complete: bool):
    if item_id not in items:
        return {"error": "The id does not exist"}
    updated_item = {
        "id": item_id,
        "title": title,
        "description": description,
        "name_item": name_item,
        "complete": complete
    }
    items[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "The id does not exist"}
    deleted_item = items.pop(item_id)
    return {"message": "Item deleted successfully", "deleted_item": deleted_item}

if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)

