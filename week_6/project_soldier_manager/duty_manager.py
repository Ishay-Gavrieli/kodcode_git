from utils import find_soldier_by_id, validate_duty_fields




def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str):
    soldier = find_soldier_by_id(soldier_id)
    
    if soldier is None:
        raise KeyError(f"Soldier ID {soldier_id} does not exist.")
        
    validate_duty_fields(soldier, duty_name, day, "pending")
    
    soldier["duties"].append({
        "name": duty_name.strip(),
        "day": day.lower().strip(),
        "status": "pending"
    })





def update_duty_status(soldier_id: int, duty_name: str, new_status: str):
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier ID {soldier_id} does not exist.")
        
    target_duty = None
    for duty in soldier["duties"]:
        if duty["name"].lower().strip() == duty_name.lower().strip():
            target_duty = duty
            break
            
    if target_duty is None:
        raise KeyError(f"Duty '{duty_name}' not found for this soldier.")
        
    validate_duty_fields({"duties": []}, "valid_name", "sunday", new_status)
    
    target_duty["status"] = new_status.lower().strip()



def get_soldier_duties(soldier_id: int) -> list:
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier ID {soldier_id} does not exist.")
    
    return soldier["duties"]