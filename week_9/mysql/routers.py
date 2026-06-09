from fastapi import APIRouter, HTTPException, Query
import queries

router = APIRouter()

@router.get("/soldiers")
def list_soldiers(
    rank: str | None = None,
    sort: str = "asc",
    unit: str | None = None
):
    if rank:
        return {"soldiers": queries.get_by_rank(rank)}
    # Add other filters as needed
    return {"soldiers": queries.get_active_sorted(sort)}

@router.get("/soldiers/search")
def search_soldiers(name: str = Query(...)):
    return {"soldiers": queries.search_by_name(name)}

@router.get("/soldiers/{soldier_id}")
def get_soldier(soldier_id: int):
    soldier = queries.get_by_id(soldier_id)
    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier

@router.post("/soldiers")
def create_soldier(name: str, rank: str, unit: str):
    if not name or name.strip() == "":
        raise HTTPException(status_code=422, detail="Name cannot be empty")
    new_id = queries.create(name, rank, unit)
    return {"id": new_id, "message": "Created successfully"}