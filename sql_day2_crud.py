# Day 2: UPDATE, DELETE, LIKE — Full CRUD

import sqlite3

# ─────────────────────────────────────────
# SETUP — fresh database every run
# ─────────────────────────────────────────
conn = sqlite3.connect("qa_practice.db")
cursor = conn.cursor()

# Drop table if exists so we start clean
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
    CREATE TABLE users (
        id       INTEGER PRIMARY KEY,
        name     TEXT    NOT NULL,
        email    TEXT    NOT NULL,
        age      INTEGER,
        is_paid  INTEGER DEFAULT 0
    )
""")

# Insert fresh test data
users_data = [
    ('Rama',   'rama@gmail.com',       22, 1),
    ('Priya',  'priya@gmail.com',      25, 0),
    ('Ravi',   'ravi@gmail.com',       17, 0),
    ('Admin',  'admin@highscores.ai',  30, 1),
    ('Kumar',  'kumar@gmail.com',      28, 0),
    ('Test',   'test@test.com',        22, 0),
]

cursor.executemany("""
    INSERT INTO users (name, email, age, is_paid)
    VALUES (?, ?, ?, ?)
""", users_data)

conn.commit()
print("✅ Fresh table created with 6 users")

# ─────────────────────────────────────────
# HELPER FUNCTION
# prints all users cleanly
# ─────────────────────────────────────────
def show_all(label):
    print(f"\n--- {label} ---")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

show_all("STARTING DATA")

# ─────────────────────────────────────────
# UPDATE — change existing data
# Syntax: UPDATE table SET column = value
#         WHERE condition
# ─────────────────────────────────────────
print("\n\n======= UPDATE =======")

# QA scenario: Priya just paid — update her status
cursor.execute("""
    UPDATE users
    SET is_paid = 1
    WHERE name = 'Priya'
""")
conn.commit()
print("✅ Updated Priya → is_paid = 1")

# Verify the change (QA mindset — always verify!)
cursor.execute("SELECT * FROM users WHERE name = 'Priya'")
print("Verified:", cursor.fetchone())

# ─────────────────────────────────────────
# ⚠️  THE #1 BEGINNER MISTAKE WITH UPDATE
# NEVER forget the WHERE clause
# ─────────────────────────────────────────
# cursor.execute("UPDATE users SET is_paid = 1")
# ↑ This updates EVERY single row!
# ↑ Never do this without WHERE
print("\n⚠️  RULE: Always use WHERE with UPDATE")
print("   Without WHERE → updates ALL rows!")

# ─────────────────────────────────────────
# UPDATE multiple columns at once
# ─────────────────────────────────────────
cursor.execute("""
    UPDATE users
    SET age = 18, is_paid = 1
    WHERE name = 'Ravi'
""")
conn.commit()
print("\n✅ Updated Ravi → age=18, is_paid=1")

cursor.execute("SELECT * FROM users WHERE name = 'Ravi'")
print("Verified:", cursor.fetchone())

show_all("AFTER UPDATES")

# ─────────────────────────────────────────
# DELETE — remove rows
# Syntax: DELETE FROM table WHERE condition
# ─────────────────────────────────────────
print("\n\n======= DELETE =======")

# QA scenario: remove test/dummy accounts
cursor.execute("""
    DELETE FROM users
    WHERE name = 'Test'
""")
conn.commit()
print("✅ Deleted test account")

# Verify it's gone
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"Users remaining: {count}")
assert count == 5, f"❌ Expected 5, got {count}"
print("✅ Count assertion passed — test account removed")

# ─────────────────────────────────────────
# ⚠️  THE #1 BEGINNER MISTAKE WITH DELETE
# ─────────────────────────────────────────
# cursor.execute("DELETE FROM users")
# ↑ Deletes EVERY row in the table!
# ↑ The table still exists but is empty
print("\n⚠️  RULE: Always use WHERE with DELETE")
print("   Without WHERE → deletes ALL rows!")

show_all("AFTER DELETE")

# ─────────────────────────────────────────
# LIKE — search/partial match
# Syntax: WHERE column LIKE 'pattern'
#
# % = wildcard (means "anything here")
# ─────────────────────────────────────────
print("\n\n======= LIKE =======")

# Find all gmail users
print("\n--- Users with Gmail ---")
cursor.execute("""
    SELECT * FROM users
    WHERE email LIKE '%gmail.com'
""")
for row in cursor.fetchall():
    print(row)

# Find emails containing 'highscores'
print("\n--- Users with highscores email ---")
cursor.execute("""
    SELECT * FROM users
    WHERE email LIKE '%highscores%'
""")
for row in cursor.fetchall():
    print(row)

# Find names starting with 'R'
print("\n--- Names starting with R ---")
cursor.execute("""
    SELECT * FROM users
    WHERE name LIKE 'R%'
""")
for row in cursor.fetchall():
    print(row)

# ─────────────────────────────────────────
# QA REAL SCENARIO — find suspicious data
# ─────────────────────────────────────────
print("\n\n======= QA CHECKS =======")

# Check 1: find test/dummy emails
print("\n--- ⚠️  QA: Suspicious test emails ---")
cursor.execute("""
    SELECT * FROM users
    WHERE email LIKE '%test%'
    OR email LIKE '%dummy%'
    OR email LIKE '%fake%'
""")
rows = cursor.fetchall()
if rows:
    print(f"❌ Found {len(rows)} suspicious account(s):")
    for row in rows:
        print(row)
else:
    print("✅ No suspicious emails found")

# Check 2: unpaid users over 25
print("\n--- QA: Unpaid users over 25 ---")
cursor.execute("""
    SELECT * FROM users
    WHERE is_paid = 0
    AND age > 25
""")
for row in cursor.fetchall():
    print(row)

# Check 3: count paid vs unpaid
print("\n--- QA: Paid vs Unpaid count ---")
cursor.execute("SELECT COUNT(*) FROM users WHERE is_paid = 1")
paid = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM users WHERE is_paid = 0")
unpaid = cursor.fetchone()[0]

print(f"Paid users   : {paid}")
print(f"Unpaid users : {unpaid}")
print(f"Total        : {paid + unpaid}")

# ─────────────────────────────────────────
conn.close()
print("\n✅ Day 2 Complete!")