import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS player")
cursor.execute("CREATE TABLE player(name, number, position)")
cursor.execute(
    """
INSERT INTO player VALUES
('Jackie Robinson', 42, '2B')
"""
)
response = cursor.execute("SELECT * FROM player")
print(response.fetchall())
cursor.close()
conn.commit()
conn.close()
