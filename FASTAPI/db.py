import sqlite3


conn = sqlite3.connect('emotion_analyzer.db',check_same_thread=False)

cursor = conn.cursor()

result = cursor.execute('''
Drop table if exists Emotion_analyzer
''')

conn.commit()
conn.close()