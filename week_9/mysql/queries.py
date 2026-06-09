import db

def get_all():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_by_id(soldier_id: int):
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create(name: str, rank: str, unit: str):
    conn = db.get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, `rank`, unit) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, rank, unit))
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def get_by_rank(rank: str):
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE `rank` = %s", (rank,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_active_sorted(order: str = "asc"):
    sort_dir = "DESC" if order.lower() == "desc" else "ASC"
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM soldiers WHERE active = TRUE ORDER BY name {sort_dir}")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def search_by_name(term: str):
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s", (f"%{term}%",))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result