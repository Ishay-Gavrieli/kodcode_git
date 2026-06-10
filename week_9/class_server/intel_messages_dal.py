import mysql.connector
import logging

logger = logging.getLogger(__name__)

class IntelMessagesDAL:
    VALID_CLASSIFICATIONS = ('unclassified', 'confidential', 'secret', 'top_secret')

    def __init__(self, host: str, user: str, password: str, database: str, logger: logging.Logger):
        self.host = host
        self.user = user 
        self.password = password
        self.database = database
        self.logger = logger
        self.conn = None
        self.cursor = None

    def get_conn(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=3306)
    
    def setup(self) -> None:
        valid = ", ".join([f"'{c}'" for c in self.VALID_CLASSIFICATIONS])
        create_table = f"CREATE TABLE IF NOT EXISTS intel_messages(id INT PRIMARY KEY AUTO_INCREMENT, unit varchar(100), classification ENUM({valid}), content varchar(100))"
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor()
            self.cursor.execute(create_table)
            self.conn.commit() 
            self.logger.info("Table 'intel_messages' created successfully.")
        except Exception as e:
            self.logger.error(f"Setup failed: {e}")
            raise e
        finally:
            self.close()

    def get_schema(self) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("DESCRIBE intel_messages")
            self.logger.info("Schema retrieved")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error getting schema: {e}")
            raise e
        finally:
            self.close()

    def get_all(self) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages")
            self.logger.info("Fetched all records")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error fetching all: {e}")
            raise e
        finally:
            self.close()

    def get_by_id(self, message_id: int) -> dict | None:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE id = %s", (message_id,))
            result = self.cursor.fetchone()
            self.logger.info(f"Fetched by id {message_id}")
            return result if result else None
        except Exception as e:
            self.logger.error(f"Error fetching by id: {e}")
            return None
        finally:
            self.close()

    def create(self, unit: str, classification: str, content: str, source: str | None) -> int:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            sql = "INSERT INTO intel_messages(unit, classification, content, source) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (unit, classification, content, source))
            result = self.cursor.lastrowid
            self.conn.commit()
            self.logger.info(f"Created new message with id: {result}")
            return result 
        except Exception as e:
            self.logger.error(f"Create failed: {e}")
            raise e
        finally:
            self.close()

    def update(self, message_id: int, data: dict) -> bool:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            sql = "UPDATE intel_messages SET unit = %s, classification = %s, content = %s WHERE id = %s"
            self.cursor.execute(sql, (data["unit"], data["classification"], data["content"], message_id))
            result = self.cursor.rowcount
            self.conn.commit()
            self.logger.info(f"Updated id: {message_id}")
            return result 
        except Exception as e:
            self.logger.error(f"Update failed: {e}")
            raise e
        finally:
            self.close()

    def delete(self, message_id: int) -> bool:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("DELETE FROM intel_messages WHERE id = %s",(message_id,))
            self.conn.commit()
            self.logger.info(f"Deleted id: {message_id}")
            return self.cursor.rowcount
        except Exception as e:
            self.logger.error(f"Delete failed: {e}")
            raise e
        finally:
            self.close()

    def get_by_unit(self, unit: str) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE unit = %s ORDER BY id DESC",(unit,))
            self.logger.info(f"Fetched by unit: {unit}")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error by unit: {e}")
            raise e
        finally:
            self.close()

    def get_by_classification(self, classification: str) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE classification = %s",(classification,))
            self.logger.info(f"Fetched by classification: {classification}")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error by classification: {e}")
            raise e
        finally:
            self.close()
    
    def get_by_unit_and_classification(self, unit: str, classification: str) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE classification = %s AND unit = %s",(classification,unit))
            self.logger.info(f"Fetched by unit and classification")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error by unit and classification: {e}")
            raise e
        finally:
            self.close()

    def get_distinct_units(self) -> list[str]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT DISTINCT unit FROM intel_messages")
            result = self.cursor.fetchall()
            self.logger.info("Fetched distinct units")
            return [u["unit"] for u in result]
        except Exception as e:
            self.logger.error(f"Error getting units: {e}")
            raise e
        finally:
            self.close()

    def search_content(self, term: str) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE content LIKE %s",(f"%{term}%",))
            self.logger.info(f"Searched content for: {term}")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            raise e
        finally:
            self.close()

    def get_missing_source(self) -> list[dict]:
        try:
            self.conn = self.get_conn()
            self.cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute("SELECT * FROM intel_messages WHERE source IS NULL")
            self.logger.info("Fetched missing source items")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error fetching missing source: {e}")
            raise e
        finally:
            self.close()

    def close(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()