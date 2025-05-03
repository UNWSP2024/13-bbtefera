import sqlite3
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS Entries (
        Name TEXT PRIMARY KEY,
        PhoneNumber TEXT)''')
conn.commit()
while True:
    print("\nPhonebook Menu:")
    print("1. Add Entry")
    print("2. Look Up Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Exit")
    choice = input("Choose an option (1–5): ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        try:
            cur.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
            conn.commit()
            print("Entry added.")
        except sqlite3.IntegrityError:
            print("Name already exists.")
    elif choice == '2':
        name = input("Enter name to look up: ")
        cur.execute("SELECT PhoneNumber FROM Entries WHERE Name = ?", (name,))
        result = cur.fetchone()
        if result:
            print(f"{name}'s number is {result[0]}")
        else:
            print("Entry not found.")
    elif choice == '3':
        name = input("Enter name to update: ")
        new_number = input("Enter new phone number: ")
        cur.execute("UPDATE Entries SET PhoneNumber = ? WHERE Name = ?", (new_number, name))
        if cur.rowcount:
            conn.commit()
            print("Phone number updated.")
        else:
            print("Entry not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
        if cur.rowcount:
            conn.commit()
            print("Entry deleted.")
        else:
            print("Entry not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
conn.close()
print("Goodbye!")
