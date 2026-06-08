import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "soldiers_db"
    )
    


def get_all()-> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    try:
        cursor.execute("SELECT * FROM soldiers")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def get_by_id(soldier_id: int) -> dict | None :
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from soldiers where id = %s",(soldier_id,))
    try:
        cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
        result = cursor.fetchone()
        return result if result else None
    finally:
        cursor.close()
        conn.close()



def create(name: str, rank: str,unit:str) -> int:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        sql = "INSERT INTO soldiers (name, `rank`,unit) VALUES (%s, %s,%s)"
        cursor.execute(sql, (name, rank,unit))
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()



def update(soldier_id, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("update soldiers set name = %s, `rank` = %s , unit = %s, WHERE id = %s",(data['name'], data['rank'],data["unit"] ,soldier_id))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Update failed: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
    




def delete(soldier_id: int) -> bool :
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM soldiers WHERE id = %s", (soldier_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()


def get_by_unit(unit_name: str) -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM soldiers WHERE unit = %s", (unit_name,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

        

def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers") 
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1]} for row in rows]


