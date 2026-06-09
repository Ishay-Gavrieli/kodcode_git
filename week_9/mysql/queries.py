import db
import logging

logger = logging.getLogger(__name__)


def get_by_id(soldier_id: int):
    try:
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        logger.error(f"Error fetching soldier {soldier_id}: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def create(name: str, rank: str, unit: str):
    try:
        conn = db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO soldiers (name, `rank`, unit) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, rank, unit))
        conn.commit()
        new_id = cursor.lastrowid
        return new_id
    except Exception as e:
        logger.error(f"Error fetching soldier: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_by_rank(rank: str):
    try:
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM soldiers WHERE `rank` = %s", (rank,))
        result = cursor.fetchall()
        return result
    except Exception as e:
        logger.error(f"Error fetching soldier: {e}")
        return None
    finally:
        cursor.close()
        conn.close()



def get_active_sorted(order: str = "asc"):
    try:
        sort_dir = "DESC" if order.lower() == "desc" else "ASC"
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM soldiers WHERE active = TRUE ORDER BY name {sort_dir}")
        result = cursor.fetchall()
        return result
    except Exception as e:
        logger.error(f"Error fetching soldier: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


def search_by_name(term: str):
    try:
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s", (f"%{term}%",))
        result = cursor.fetchall()
        return result
    except Exception as e:
        logger.error(f"Error fetching soldier: {e}")
        return None
    finally:
        cursor.close()
        conn.close()



def get_by_unit(unit:str):
    try:
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM soldiers WHERE unit = %s",(unit,))
        result = cursor.fetchall()
        return result
    except Exception as e:
        logger.error(f"Error fetching soldier: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
    