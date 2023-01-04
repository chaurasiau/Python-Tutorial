import sqlite3
dbName = 'database.db'


def insert_command(conn, student_id, name, surname):
    command = 'INSERT INTO student VALUES (?, ?, ?)'
    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        cur.execute(command, (student_id, name, surname, ))
        cur.execute("COMMIT")
    except conn.Error as e:
        print("Got an error: ", e)
        print("Aborting...")
        cur.execute("ROLLBACK")


conn = sqlite3.connect(dbName, isolation_level=None)
cursor = conn.cursor()
print("Database created!")

# Create operation
create_query = '''CREATE TABLE IF NOT EXISTS student(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT NOT NULL);
  '''
cursor.execute(create_query)
print("Table created!")

# Insert and Read operation
insert_command(conn, 1, 'John', 'Smith')
insert_command(conn, 2, 'Lucy', 'Jacobs')
insert_command(conn, 3, 'Stephan', 'Taylor')
insert_command(conn, 4, 'Joseph', 'Random')
findRecords = cursor.execute("SELECT * FROM student")
for row in findRecords:
    print(row)

conn.close()
