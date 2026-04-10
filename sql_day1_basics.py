# sql_day1_basics.py
# Week 6 - SQL for QA Engineers
# Day 1: Creating tables, inserting data, basic queries

import sqlite3

# STEP 1: Connect to a database
# (Creates the file if it doesn't exist)

conn = sqlite3.connect("qa_practice.db")
cursor = conn.cursor()
print("✅ Connected to database")

# STEP 2: CREATE TABLE

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id       INTEGER PRIMARY KEY,
        name     TEXT    NOT NULL,
        email    TEXT    NOT NULL,
        age      INTEGER,
        is_paid  INTEGER DEFAULT 0
    )
""")
print("✅ Table 'users' created")

cursor.execute("DELETE FROM users")


# STEP 3: INSERT rows (add test data)

cursor.execute("""
    INSERT INTO users (name, email, age, is_paid)
    VALUES ('Rama', 'rama@gmail.com', 22, 1)
""")

cursor.execute("""
    INSERT INTO users (name, email, age, is_paid)
    VALUES ('Priya', 'priya@gmail.com', 25, 0)
""")

cursor.execute("""
    INSERT INTO users (name, email, age, is_paid)
    VALUES ('Ravi', 'ravi@gmail.com', 17, 0)
""")

cursor.execute("""
    INSERT INTO users (name, email, age, is_paid)
    VALUES ('Admin', 'admin@highscores.ai', 30, 1)
""")

conn.commit()
print("✅ 4 users inserted")

# STEP 4: SELECT — Read data back
# This is your #1 most-used SQL command

print("\n--- ALL USERS ---")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# STEP 5: SELECT with WHERE — Filter data
# QA use: "Show me only paid users"

print("\n--- PAID USERS ONLY ---")
cursor.execute("SELECT * FROM users WHERE is_paid = 1")
rows = cursor.fetchall()
for row in rows:
    print(row)

# STEP 6: QA CHECK — underage users
# Real scenario: DOB/age validation bug
# (You found this in HighScores.ai!)

print("\n--- ⚠️  QA CHECK: USERS UNDER 18 ---")
cursor.execute("SELECT * FROM users WHERE age < 18")
rows = cursor.fetchall()
if rows:
    print(f"BUG FOUND ❌ — {len(rows)} underage user(s) in system:")
    for row in rows:
        print(row)
else:
    print("✅ No underage users found")

# STEP 7: COUNT — How many rows?
# QA use: "Did all 4 records insert?"

print("\n--- ROW COUNT CHECK ---")
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"Total users in DB: {count}")
assert count == 4, f"❌ Expected 4 users, got {count}"
print("✅ Count assertion passed")

# CLEANUP

conn.close()
print("\n✅ Day 1 Complete — Database connection closed")