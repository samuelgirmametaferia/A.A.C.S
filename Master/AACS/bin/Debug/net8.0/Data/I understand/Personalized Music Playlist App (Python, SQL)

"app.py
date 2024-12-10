import sqlite3

conn = sqlite3.connect('music_db.sqlite')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    mood TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist TEXT,
    genre TEXT
)''')

# ... (Code to add songs and user data)

def get_playlist(mood):
  cursor.execute(f"SELECT title FROM songs WHERE genre = ?", (mood,))
  songs = cursor.fetchall()
  return songs

# ... (Code to handle user input and generate playlists)

conn.commit()
conn.close()