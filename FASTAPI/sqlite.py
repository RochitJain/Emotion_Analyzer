import sqlite3
from datetime import datetime,timezone

conn = sqlite3.connect('emotion_analyze.db',check_same_thread=False)

cursor = conn.cursor()

def insert(name,sentiment,text):
    emotion = sentiment["emotion"]
    polarity = sentiment["polarity"]
    subjectivity = sentiment["subjectivity"]
    created_at = datetime.now(timezone.utc).isoformat()
    cursor.execute('''
        INSERT INTO Emotion_analyze(name,text,emotion,polarity,subjectivity,created_at)
                    VALUES(?,?,?,?,?,?)''',(name,text,emotion,polarity,subjectivity,created_at))
    conn.commit()
    entry_id = cursor.lastrowid
    print('Data inserted successfully')
    return entry_id

def view(limit:int = 200):
    cursor.execute("SELECT * FROM Emotion_analyze ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    return [
        {
            "id": r[0],
            "name": r[1],
            "text": r[2],
            "emotion": r[3],
            "polarity": r[4],
            "subjectivity": r[5],
            "created_at": r[6]
        }
        for r in rows
    ]
