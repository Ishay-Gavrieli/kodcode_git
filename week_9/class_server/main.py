from fastapi import FastAPI
from intel_messages_dal import IntelMessagesDAL
from basic_logger import logger
import uvicorn

app = FastAPI()

intel = IntelMessagesDAL("localhost","root","root","soldiers_db",logger)

@app.get("/schema")
def schema():
    logger.info("Accessing database schema")
    return intel.get_schema()

@app.get("/soldiers")
def all_soldiers():
    logger.info("Fetching all soldiers")
    return intel.get_all()

@app.get("/messages/{message_id}")
def all_soldiers(message_id:int):
    logger.info(f"Fetching message by id: {message_id}")
    return intel.get_by_id(message_id)

@app.post("/messages")
def all_soldiers(unit: str, classification: str, content: str, source: str | None):
    logger.info(f"Creating new message for unit: {unit}")
    return intel.create(unit,classification,content,source)

@app.put("/messages/{message_id}")
def update(message_id: int, data: dict):
    logger.info(f"Updating message id: {message_id}")
    return intel.update(message_id,data)

@app.get("/massages/units")
def all_units():
    logger.info("Fetching all units")
    return intel.get_distinct_units()

@app.get("/massages/search")
def search_by_term(term: str):
    logger.info(f"Searching content for term: {term}")
    return intel.search_content(term)

@app.get("/messages/missing-source")
def missing_source():
    logger.info("Fetching messages with missing source")
    return intel.get_missing_source()

@app.delete("/messages/{message_id}")
def delete_by_id(message_id: int):
    logger.info(f"Deleting message id: {message_id}")
    return intel.delete(message_id)

if __name__=="__main__":
    logger.info("Starting server")
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)