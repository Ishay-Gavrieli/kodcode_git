from fastapi import APIRouter,HTTPException
import db

router = APIRouter()


@router.get("/schema")
def get_schema():
    columns = db.get_schema()
    return {"columns": columns}

@router.get("/soldiers")
def get_all_soldiers():
    soldier = db.get_all()
    return soldier


@router.get("/soldiers/{soldier_id}")
def get_all_soldiers(soldier_id):
    soldier = db.get_by_id(soldier_id)
    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier



@router.post("/soldiers")
def create_soldier(name: str, rank: str, unit: str):
    if not name or name.strip() == "":
        raise HTTPException(status_code=422, detail="Name cannot be empty")
    
    return db.create(name, rank, unit)
    

@router.put("/soldiers/{soldier_id}")
def update_soldier(soldier_id:int, data: dict):
    success = db.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated successfully"}



@router.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id:int):
    success = db.delete(soldier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted successfully"}



@router.get("/soldiers/unit/{unit_name}")
def get_soldiers_by_unit(unit_name: str):
    return db.get_by_unit(unit_name)