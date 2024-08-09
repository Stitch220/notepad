import sqlite3
from datetime import datetime

def create_database_connection(): # establish a connection to database. If the database doesn't exist, it will be created.
    try:
        conn = sqlite3.connect('notes.db')
        return conn
    except sqlite3.Error as err:
        print(f"Error connecting to database: {err}")
        return None
    
def create_notes_table(): # creates note table in database
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                body TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating notes table: {err}")

def execute_query(query, params=None): # executes SQL querys and return results
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    except sqlite3.Error as err:
        print(f"Error executing query: {err}")
        return []
    
def create_note(title='', body=''): # create a new note
    insert_query = "INSERT INTO notes (title, body) VALUES (?, ?)"
    params = (title, body)
    execute_query(insert_query, params)
    print("Note created successfully!")

def get_note(note_id): # retrive a single note, specified by note_id
    select_quary = "SELECT * FROM notes WHERE id = ?"
    params = (note_id,)
    results = execute_query(select_quary, params)
    if len(results) == 1:
        print(f"Retrived note {note_id} successfully.")
        result = results[0]
    else:
        print(f"Note {note_id} not found!")
        result = None
    return result

def get_all_notes(): # retrive all notes, ordered by their update time
    select_query = "SELECT * FROM notes ORDER BY updated_at DESC"
    results = execute_query(select_query)
    print(f"Retrieved {len(results)} note(s) successfully.")
    return results

def update_note(note_id, new_title, new_body): # updates an existing note with a new title and body content
    update_quary = "UPDATE notes SET title = ?, body = ?, update_at = ? WHERE id = ?"
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    params = (new_title, new_body, now, note_id)
    execute_query(update_quary, params)
    print(f"Updated note {note_id} successfully!")

def delete_note(note_id): # delete a note permanently from database
    delete_quary = "DELETE FROM notes WHERE id = ?"
    params = (note_id)
    execute_query(delete_quary, params)
    print(f"Deleted note {note_id} successfully!")

def get_last_note_id(): # return the id of the most recently updated note
    select_query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT 1"
    results = execute_query(select_query)
    note = results[0]
    note_id = note[0]
    print(f"Retrieved most recently updated note successfully!")
    return note_id

