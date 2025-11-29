from .database import get_db

def get_all_students():
    db = get_db()
    return db.execute("SELECT * FROM students").fetchall()

def add_student(name, email):
    db = get_db()
    db.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
    db.commit()

def get_student(id):
    db = get_db()
    return db.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()

def update_student(id, name, email):
    db = get_db()
    db.execute("UPDATE students SET name=?, email=? WHERE id=?", (name, email, id))
    db.commit()

def delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
