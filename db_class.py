import sqlite3

class budget:
    """
    A class to represent a database connection to the budget database. 
    This database is an sqlite3 database. 
    Attributes: 
    ----------
    path: str
        This is the path to the db
    
    Methods:
    -------
    create_table():
        This function creates the table named budget if
        it does not exist
    update_table()
        Updating an entry in the database 
    
    
    
    """
    def __init__(self, path: str) -> None:
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
    
    def create_table(self) -> None:
        self.cur.execute("""CREATE TABLE IF NOT EXISTS budget(
            id INTEGER PRIMARY KEY,
            date DATE, 
            value REAL,
            category TEXT,
            description TEXT
        )""")
    
    def update_table(self, id: int, colname: str, value) -> None:
        exstring = """
        UPDATE budget
        SET
        {c} = {v}
        WHERE
        id = {i}
        """
        self.cur.execute(exstring.format(c = colname, v = value, i = id))

    def add_entry(self, data: list) -> None:
        self.cur.executemany("""
            INSERT OR IGNORE INTO products VALUES(?, ?, ?, ?, ?)
        """, data)
        self.con.commit()

    def close(self) -> None:
        self.con.close()
