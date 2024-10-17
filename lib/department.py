from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        '''Creates the departments table if it doesn't exist.'''
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        );
        """
        CURSOR.execute(create_table_sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        '''Drops the departments table if it exists.'''
        drop_table_sql = "DROP TABLE IF EXISTS departments;"
        CURSOR.execute(drop_table_sql)
        CONN.commit()

    def save(self):
        '''Saves a Department instance to the db and assigns the instance an id.'''
        save_sql = """
        INSERT INTO departments (name, location)
        VALUES (?, ?)
        """
        CURSOR.execute(save_sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        '''Creates a new row in the db using parameter data and returns a Department instance.'''
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        '''Updates an instance's corresponding db row to match its new attribute values.'''
        update_sql = """
        UPDATE departments
        SET name = ?, location = ?
        WHERE id = ?
        """
        CURSOR.execute(update_sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        '''Deletes the instance's corresponding db row.'''
        delete_sql = "DELETE FROM departments WHERE id = ?;"
        CURSOR.execute(delete_sql, (self.id,))
        CONN.commit()





