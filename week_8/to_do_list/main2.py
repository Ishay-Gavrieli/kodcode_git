# question 1
import requests

data = requests.get("https://jsonplaceholder.typicode.com/users/1").json()

name = data["name"]
email = data["email"]
city = data["address"]["city"]

print(f"Name: {name}")
print(f"Email: {email}")
print(f"City: {city}")


add1 = requests.get("https://jsonplaceholder.typicode.com/posts").json()

print(len(add1))


add2 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2").json()

for post in add2:
    print(post["title"])




question 2
import requests

def safe_get(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    elif response.status_code == 404:
        return None
    
    else:
        raise Exception(f"error:request faild with status {response.status_code}")
    


question 3
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
def greet_user(name:str):
    return {"message": f"Hello, {name}!"}



if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)


question 4

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


items = {"1":{"id":0,
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
def create_item():
    


@app.put("/items/{item_id}")
def update_item(item_id:int):
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    pass



if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)

