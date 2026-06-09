import logging
from fastapi import APIRouter, HTTPException, Query
import queries

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/soldiers")
def get_soldiers(
    rank: str | None = None,
    unit: str | None = None,
    sort: str = "asc"
):
    logger.info(f"Fetching soldiers list with filters: rank={rank}, unit={unit}, sort={sort}")
    try:
        if rank:
            return {"soldiers": queries.get_by_rank(rank)}
        if unit:
            return {"soldiers": queries.get_by_unit(unit)}
        return {"soldiers": queries.get_active_sorted(sort)}
    except Exception as e:
        logger.error(f"Error fetching soldiers: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/soldiers/search")
def search_soldiers(name: str = Query(...)):
    logger.info(f"Searching for soldiers with term: {name}")
    try:
        return {"soldiers": queries.search_by_name(name)}
    except Exception as e:
        logger.error(f"Error searching soldiers for '{name}': {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/soldiers/{soldier_id}")
def get_soldier(soldier_id: int):
    logger.info(f"Fetching soldier details for ID: {soldier_id}")
    try:
        soldier = queries.get_by_id(soldier_id)
        if not soldier:
            logger.warning(f"Soldier with ID {soldier_id} not found.")
            raise HTTPException(status_code=404, detail="Soldier not found")
        return soldier
    except HTTPException:
        raise 
    except Exception as e:
        logger.error(f"Error fetching soldier {soldier_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/soldiers")
def create_soldier(name: str, rank: str, unit: str):
    logger.info(f"Attempting to create soldier: {name}")
    
    if not name or name.strip() == "":
        logger.warning("Attempted to create soldier with empty name")
        raise HTTPException(status_code=422, detail="Name cannot be empty")
        
    try:
        new_id = queries.create(name, rank, unit)
        logger.info(f"Soldier created successfully with ID: {new_id}")
        return {"id": new_id, "message": "Created successfully"}
    except Exception as e:
        logger.error(f"Failed to create soldier: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")