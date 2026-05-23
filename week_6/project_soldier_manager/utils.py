from data import data



def find_soldier_by_id(soldier_id: int) -> dict:
    for soldier in data:
        if soldier["id"] == soldier_id:
            return soldier
    return None




def validate_new_soldier(soldier_id: int, name: str):
    if soldier_id < 0 or len(str(soldier_id)) != 7:
        raise ValueError("ID must be a positive 7-digit number.")
    
    if find_soldier_by_id(soldier_id) is not None:
        raise ValueError(f"Soldier ID {soldier_id} already exists.")
    
    if not name:
        raise ValueError("Soldier name cannot be empty.")
        
    if not name.isalpha():
        raise ValueError("Soldier name must contain letters only.")
    



def validate_duty_fields(soldier_dict: dict, duty_name: str, day: str, status: str):
    if not duty_name:
        raise ValueError("Duty name cannot be empty.")
    
    for duty in soldier_dict["duties"]:
        if duty["name"].lower().strip() == duty_name.lower().strip():
            raise ValueError(f"Soldier already has a duty named '{duty_name.strip()}'.")


    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    day_clean = day.lower().strip()
    
    if day_clean in ["friday", "saturday"]:
        raise ValueError("Cannot assign duties on Friday or Saturday.")
    
    if day_clean not in valid_days:
        raise ValueError("Invalid day. Must be Sunday through Thursday.")

    valid_statuses = ["pending", "completed", "missed"]
    
    if status.lower().strip() not in valid_statuses:
        raise ValueError("Invalid status. Must be 'pending', 'completed', or 'missed'.")