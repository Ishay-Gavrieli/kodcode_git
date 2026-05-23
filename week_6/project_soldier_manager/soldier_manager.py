from data import data
from utils import find_soldier_by_id, validate_new_soldier



def add_soldier(soldier_id: int, name: str):
    validate_new_soldier(soldier_id, name)
    
    data.append({
        "id": soldier_id,
        "name": name.strip(),
        "duties": []
    })



def remove_soldier(soldier_id: int):
    soldier = find_soldier_by_id(soldier_id)
    
    if soldier is None:
        raise KeyError(f"Soldier ID {soldier_id} does not exist.")
        
    data.remove(soldier)

    

def get_all_soldiers() -> list:
    return data