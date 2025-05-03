import sqlite3

conn = sqlite3.connect('cities.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Cities')
cur.execute('''
    CREATE TABLE Cities (
        CityID INTEGER PRIMARY KEY,
        CityName TEXT,
        Population INTEGER
    )
''')

cities = [
    (1, 'Tokyo', 38001000), (2, 'Delhi', 25703168), (3, 'Shanghai', 23740778),
    (4, 'Sao Paulo', 21066245), (5, 'Mumbai', 21042538), (6, 'Mexico City', 20998543),
    (7, 'Beijing', 20383994), (8, 'Osaka', 20237645), (9, 'Cairo', 18771769),
    (10, 'New York', 18593220), (11, 'Dhaka', 17598228), (12, 'Karachi', 16617644),
    (13, 'Buenos Aires', 15180176), (14, 'Kolkata', 14864919), (15, 'Istanbul', 14163989),
    (16, 'Chongqing', 13331579), (17, 'Lagos', 13122829), (18, 'Manila', 12946263),
    (19, 'Rio de Janeiro', 12902306), (20, 'Guangzhou', 12458130)
]

cur.executemany('INSERT INTO Cities VALUES (?, ?, ?)', cities)
conn.commit()

print("CityID  City Name           Population")
print("------------------------------------------")
for city in cur.execute('SELECT * FROM Cities'):
    print(f"{city[0]:<7} {city[1]:<20} {city[2]:,}")

conn.close()
#instructions were very confusing for all programs
