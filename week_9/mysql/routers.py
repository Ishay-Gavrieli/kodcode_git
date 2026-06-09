from fastapi import APIRouter,HTTPException,Query   
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
    

@router.put("/{soldier_id}")
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



@router.get("/active_soldiers")
def get_active(order: str = "asc"):
    return db.get_active_sorted(order)



@router.get("/distinct_units")
def distinct_units():
    data = db.get_distinct_units()
    return data



@router.get("/not_null")
def rank_not_null():
    data = db.not_null()
    return data






@router.get("/soldiers")
def list_soldiers(
    rank: str | None = Query(default=None),
    sort: str = Query(default="asc")
    ):
    if rank:
        return {"soldiers": db.get_by_rank(rank)}
    return {"soldiers": db.get_active_sorted(sort)}


@router.get("/soldiers/search")
def search_soldiers(name: str = Query(...)):
    return {"soldiers": db.search_by_name(name)}