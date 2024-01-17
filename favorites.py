import sqlite3

con = sqlite3.connect("favorites.db")
db = con.cursor()
print('connected to database')

languageName = input('language : ')

# rows = db.execute("UPDATE favorites SET language = 'c' WHERE language LIKE '%c'")

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE language = ?", [languageName])

print(rows.fetchall()[0])

# for row in rows:
#     print(row)

con.close