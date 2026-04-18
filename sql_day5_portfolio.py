# sql_day5_portfolio.py
# Week 6 - SQL for QA Engineers
# Day 5: Complete Portfolio Script
# Author: Garala Ramakrishna
#
# What this script covers:
# → Database setup with realistic test data
# → Full CRUD operations
# → NULL checks and data validation
# → Duplicate detection
# → JOIN across two tables
# → $0.00 payment bug detection
# → All results printed as QA reports

import sqlite3

# ─────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────

conn = sqlite3.connect("portfolio_qa.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute("""
    CREATE TABLE users (
        id        INTEGER PRIMARY KEY,
        name      TEXT    NOT NULL,
        email     TEXT,
        age       INTEGER,
        city      TEXT,
        plan      TEXT    DEFAULT 'free'
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        id        INTEGER PRIMARY KEY,
        user_id   INTEGER,
        amount    REAL,
        status    TEXT,
        plan_type TEXT
    )
""")

print("✅ Tables created\n")

# ─────────────────────────────────────────
# INSERT — realistic + buggy data
# ─────────────────────────────────────────

users = [
    ('Rama',   'rama@gmail.com',    22, 'Hyderabad', 'premium'),
    ('Priya',  'priya@gmail.com',   25, 'Hyderabad', 'free'),
    ('Ravi',   'ravi@gmail.com',    17, 'Mumbai',    'free'),
    ('Kumar',  'kumar@gmail.com',   28, 'Hyderabad', 'premium'),
    ('Sneha',  'priya@gmail.com',   23, 'Chennai',   'free'),  # duplicate email
    ('Ghost',  None,                25, 'Pune',      'free'),  # NULL email
    ('Rohan',  'rohan@gmail.com',   None,'Delhi',    'premium'),# NULL age
    ('Admin',  'admin@test.com',    30, 'Hyderabad', 'premium'),# test account
    ('Zara',   'zara@gmail.com',    22, 'Mumbai',    'free'),
    ('Dev',    'dev@gmail.com',     26, 'Bangalore', 'premium'),
]

orders = [
    (1, 999.00,  'completed', 'premium'),
    (2, 0.00,    'completed', 'premium'),  # $0 bug!
    (3, 499.00,  'pending',   'premium'),
    (4, 999.00,  'completed', 'premium'),
    (1, 0.00,    'completed', 'premium'),  # $0 bug!
    (9, 299.00,  'completed', 'free'),
    (10, 999.00, 'completed', 'premium'),
    (7, 999.00,  'completed', 'premium'),
]

cursor.executemany(
    "INSERT INTO users (name,email,age,city,plan) VALUES (?,?,?,?,?)",
    users
)
cursor.executemany(
    "INSERT INTO orders (user_id,amount,status,plan_type) VALUES (?,?,?,?)",
    orders
)
conn.commit()
print("✅ Test data inserted\n")

# ═════════════════════════════════════════
# QA REPORT — DATA VALIDATION CHECKS
# ═════════════════════════════════════════

print("=" * 55)
print("         QA DATABASE VALIDATION REPORT")
print("         Platform: QA Practice DB")
print("         Tester  : Garala Ramakrishna")
print("=" * 55)

bugs_found = 0

# ─────────────────────────────────────────
# CHECK 1: Total record count
# ─────────────────────────────────────────
print("\n[CHECK 1] Record Count")
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM orders")
order_count = cursor.fetchone()[0]
print(f"  Users  : {user_count}")
print(f"  Orders : {order_count}")

# ─────────────────────────────────────────
# CHECK 2: NULL fields
# ─────────────────────────────────────────
print("\n[CHECK 2] NULL Data Validation")
cursor.execute("""
    SELECT id, name, email, age
    FROM users
    WHERE email IS NULL OR age IS NULL
""")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ FAIL — {len(rows)} user(s) with NULL fields:")
    for r in rows:
        print(f"     {r}")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — No NULL fields found")

# ─────────────────────────────────────────
# CHECK 3: Underage users
# ─────────────────────────────────────────
print("\n[CHECK 3] Age Validation (min age: 18)")
cursor.execute("SELECT id, name, age FROM users WHERE age < 18")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ FAIL — {len(rows)} underage user(s):")
    for r in rows:
        print(f"     {r}")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — All users are 18+")

# ─────────────────────────────────────────
# CHECK 4: Duplicate emails
# ─────────────────────────────────────────
print("\n[CHECK 4] Duplicate Email Detection")
cursor.execute("""
    SELECT email, COUNT(*) as count
    FROM users
    WHERE email IS NOT NULL
    GROUP BY email
    HAVING COUNT(*) > 1
""")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ FAIL — {len(rows)} duplicate email(s):")
    for r in rows:
        print(f"     {r[0]} appears {r[1]} times")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — All emails are unique")

# ─────────────────────────────────────────
# CHECK 5: $0.00 payment bypass
# Same as HighScores.ai BUG-005
# ─────────────────────────────────────────
print("\n[CHECK 5] Payment Amount Validation")
cursor.execute("""
    SELECT o.id, u.name, u.email, o.amount, o.status
    FROM orders o
    JOIN users u ON o.user_id = u.id
    WHERE o.amount = 0.00
    AND o.status = 'completed'
""")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ CRITICAL — {len(rows)} completed order(s) with $0.00:")
    for r in rows:
        print(f"     Order#{r[0]} | {r[1]} | {r[2]} | ₹{r[3]}")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — No zero-amount completed orders")

# ─────────────────────────────────────────
# CHECK 6: Test/dummy accounts
# ─────────────────────────────────────────
print("\n[CHECK 6] Test Account Detection")
cursor.execute("""
    SELECT id, name, email FROM users
    WHERE LOWER(name) IN ('admin','test','dummy','guest')
    OR email LIKE '%test%'
    OR email LIKE '%dummy%'
""")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ FAIL — {len(rows)} test account(s) found:")
    for r in rows:
        print(f"     {r}")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — No test accounts found")

# ─────────────────────────────────────────
# CHECK 7: Free plan users with premium orders
# Data mismatch between tables
# ─────────────────────────────────────────
print("\n[CHECK 7] Plan Mismatch Detection")
cursor.execute("""
    SELECT u.name, u.plan, o.plan_type, o.amount
    FROM users u
    JOIN orders o ON u.id = o.user_id
    WHERE u.plan = 'free'
    AND o.plan_type = 'premium'
""")
rows = cursor.fetchall()
if rows:
    print(f"  ❌ FAIL — {len(rows)} plan mismatch(es):")
    for r in rows:
        print(f"     {r[0]} | user={r[1]} | order={r[2]} | ₹{r[3]}")
    bugs_found += len(rows)
else:
    print("  ✅ PASS — No plan mismatches")

# ─────────────────────────────────────────
# SUMMARY REPORT
# ─────────────────────────────────────────
print("\n" + "=" * 55)
print("  SUMMARY")
print("=" * 55)
cursor.execute("SELECT COUNT(*) FROM users")
print(f"  Total users    : {cursor.fetchone()[0]}")
cursor.execute("SELECT COUNT(*) FROM orders")
print(f"  Total orders   : {cursor.fetchone()[0]}")
cursor.execute(
    "SELECT SUM(amount) FROM orders WHERE status='completed'"
)
revenue = cursor.fetchone()[0]
print(f"  Total revenue  : ₹{revenue}")
cursor.execute("SELECT COUNT(*) FROM users WHERE plan='premium'")
print(f"  Premium users  : {cursor.fetchone()[0]}")
print(f"\n  Total bugs found : {bugs_found}")

if bugs_found == 0:
    print("  Status : ✅ ALL CHECKS PASSED")
else:
    print(f"  Status : ❌ {bugs_found} ISSUE(S) NEED ATTENTION")

print("=" * 55)

# ─────────────────────────────────────────
# CRUD DEMONSTRATION
# ─────────────────────────────────────────
print("\n\n--- CRUD OPERATIONS ---")

# UPDATE — fix Ravi's age
cursor.execute("UPDATE users SET age = 18 WHERE name = 'Ravi'")
conn.commit()
cursor.execute("SELECT name, age FROM users WHERE name = 'Ravi'")
print(f"UPDATE: Ravi age fixed → {cursor.fetchone()}")

# DELETE — remove test account
cursor.execute("DELETE FROM users WHERE LOWER(name) = 'admin'")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM users WHERE LOWER(name)='admin'")
print(f"DELETE: Admin removed → {cursor.fetchone()[0]} remaining")

# VERIFY final count
cursor.execute("SELECT COUNT(*) FROM users")
print(f"SELECT: Final user count → {cursor.fetchone()[0]}")

# ─────────────────────────────────────────
conn.close()
print("\n✅ Day 5 Complete — Week 6 SQL Done!")
print("   github.com/GaralaRamaKrishna/selenium-qa-practice")