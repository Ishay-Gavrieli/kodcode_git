from fastapi import FastAPI
import db_connect

app = FastAPI()

@app.post("/setup")
def run_setup():
    return {"status": "setup triggered"}


@app.get("/schema")
def get_schema():
    columns = db_connect.get_schema()
    return {"columns": columns}

@app.get("/soldiers")
def get_all_soldiers():
    return {"soldiers": []}

