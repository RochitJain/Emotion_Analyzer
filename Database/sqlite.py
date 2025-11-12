import sqlite3

conn = sqlite3.connect('emotion_analyzer.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Emotion_analyzer(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               emotion TEXT NOT NULL,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

def run():
    print('Choose an option')
    print('1. Insert')
    print('2. View')
    print('3. Exit')
    option = input('Enter your choice: ')
    if option == '1':
        name= input('Enter your name')
        emotion = input('Whats your emotion')
        insert(name,emotion)
    elif option == '2':
        view()
    elif option == '3':
        exit()
    else:
        print('Invalid choice')
        run()
    
def insert(name,emotion):
    cursor.execute("INSERT INTO Emotion_analyzer(name,emotion) VALUES(?,?)",(name,emotion))
    conn.commit()
    print('Data inserted successfully')
    run()

def view():
    cursor.execute("SELECT * FROM Emotion_analyzer")
    for row in cursor.fetchall():
        print(row)

def exit():
    conn.close()

run()