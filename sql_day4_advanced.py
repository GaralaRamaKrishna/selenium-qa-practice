# sql_day4_advanced.py
# Week 6 - SQL for QA Engineers
# Day 4: Advanced QA Queries

import sqlite3

conn = sqlite3.connect("qa_day4.db")
cursor = conn.cursor()

# ─────────────────────────────────────────
# SETUP — realistic test data
# More messy than before — on purpose
# Real databases always have dirty data
# ─────────────────────────────────────────

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute("""
    CREATE TABLE users (
        id       INTEGER PRIMARY KEY,
        name     TEXT,
        email    TEXT,
        age      INTEGER,
        city     TEXT,
        is_paid  INTEGER DEFAULT 0
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        id         INTEGER PRIMARY KEY,
        user_id    INTEGER,
        amount     REAL,
        status     TEXT
    )
""")

# Intentionally messy data — has bugs in it
users_data = [
    ('Rama',   'rama@gmail.com',       22, 'Hyderabad', 1),
    ('Priya',  'priya@gmail.com',      25, 'Hyderabad', 0),
    ('Ravi',   'ravi@gmail.com',       17, 'Mumbai',    0),
    ('Kumar',  'kumar@gmail.com',      28, 'Hyderabad', 1),
    ('Sneha',  'priya@gmail.com',      23, 'Chennai',   0), # duplicate email!
    ('Admin',  'admin@test.com',       30, 'Hyderabad', 1), # test account!
    ('Ghost',   None,                  25, 'Pune',      0), # NULL email!
    ('Rohan',  'rohan@gmail.com',      None, 'Delhi',   1), # NULL age!
    ('Priya',  'priya2@gmail.com',     25, 'Hyderabad', 0), # duplicate name!
    ('Zara',   'zara@gmail.com',       22, 'Mumbai',    0),
]

cursor.executemany("""
    INSERT INTO users (name, email, age, city, is_paid)
    VALUES (?, ?, ?, ?, ?)
""", users_data)

orders_data = [
    (1, 999.00, 'completed'),   # Rama
    (2, 0.00,   'completed'),   # Priya — $0 order! (your bug!)
    (3, 499.00, 'pending'),     # Ravi
    (4, 999.00, 'completed'),   # Kumar
    (1, 299.00, 'completed'),   # Rama again — 2 orders
    (5, 199.00, 'failed'),      # Sneha
    (1, 0.00,   'completed'),   # Rama — another $0 order!
]

cursor.executemany("""
    INSERT INTO orders (user_id, amount, status)
    VALUES (?, ?, ?)
""", orders_data)

conn.commit()
print("✅ Setup complete — messy data loaded\n")


# ─────────────────────────────────────────
# QUERY 1: ORDER BY — sort results
# Syntax: ORDER BY column ASC/DESC
# ─────────────────────────────────────────
print("=" * 50)
print("QUERY 1: ORDER BY — sort by age")
print("=" * 50)

cursor.execute("""
    SELECT name, age, city
    FROM users
    ORDER BY age ASC
""")
for row in cursor.fetchall():
    print(row)

# QA use: find youngest users first
# spot underage ones immediately


# ─────────────────────────────────────────
# QUERY 2: DISTINCT — remove duplicates
# Syntax: SELECT DISTINCT column FROM table
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QUERY 2: DISTINCT — unique cities")
print("=" * 50)

cursor.execute("""
    SELECT DISTINCT city FROM users
    ORDER BY city ASC
""")
for row in cursor.fetchall():
    print(row)

# QA use: check what unique values exist
# useful for dropdowns and categories


# ─────────────────────────────────────────
# QUERY 3: GROUP BY + COUNT
# Syntax: GROUP BY column
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QUERY 3: GROUP BY — users per city")
print("=" * 50)

cursor.execute("""
    SELECT city, COUNT(*) as total
    FROM users
    GROUP BY city
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(row)

# QA use: verify distribution of data
# e.g. check no city has unexpected count


# ─────────────────────────────────────────
# QUERY 4: IS NULL — find missing data
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QA CHECK 1: NULL emails and ages")
print("=" * 50)

cursor.execute("""
    SELECT id, name, email, age
    FROM users
    WHERE email IS NULL OR age IS NULL
""")
rows = cursor.fetchall()
if rows:
    print(f"❌ BUG: Found {len(rows)} users with NULL data:")
    for row in rows:
        print(row)
else:
    print("✅ No NULL data found")


# ─────────────────────────────────────────
# QUERY 5: Find DUPLICATE emails
# This is a classic QA database check
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QA CHECK 2: Duplicate emails")
print("=" * 50)

cursor.execute("""
    SELECT email, COUNT(*) as count
    FROM users
    WHERE email IS NOT NULL
    GROUP BY email
    HAVING COUNT(*) > 1
""")
rows = cursor.fetchall()
if rows:
    print(f"❌ BUG: Found {len(rows)} duplicate email(s):")
    for row in rows:
        print(row)
else:
    print("✅ No duplicate emails")


# ─────────────────────────────────────────
# QUERY 6: $0.00 orders — your exact bug!
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QA CHECK 3: Zero amount orders")
print("=" * 50)

cursor.execute("""
    SELECT o.id, u.name, u.email, o.amount, o.status
    FROM orders o
    JOIN users u ON o.user_id = u.id
    WHERE o.amount = 0.00
    AND o.status = 'completed'
""")
rows = cursor.fetchall()
if rows:
    print(f"❌ CRITICAL BUG: {len(rows)} completed orders with $0.00!")
    for row in rows:
        print(row)
else:
    print("✅ No zero-amount completed orders")


# ─────────────────────────────────────────
# QUERY 7: JOIN — connect two tables
# Syntax: JOIN table ON condition
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QUERY 7: JOIN — users with orders")
print("=" * 50)

cursor.execute("""
    SELECT u.name, u.email, o.amount, o.status
    FROM users u
    JOIN orders o ON u.id = o.user_id
    ORDER BY u.name ASC
""")
for row in cursor.fetchall():
    print(row)


# ─────────────────────────────────────────
# QUERY 8: SUM and AVG
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QUERY 8: SUM and AVG of orders")
print("=" * 50)

cursor.execute("""
    SELECT
        COUNT(*)            as total_orders,
        SUM(amount)         as total_revenue,
        AVG(amount)         as avg_order_value,
        MIN(amount)         as min_order,
        MAX(amount)         as max_order
    FROM orders
    WHERE status = 'completed'
""")
row = cursor.fetchone()
print(f"Total orders   : {row[0]}")
print(f"Total revenue  : ₹{row[1]}")
print(f"Average order  : ₹{row[2]:.2f}")
print(f"Min order      : ₹{row[3]}")
print(f"Max order      : ₹{row[4]}")


# ─────────────────────────────────────────
# QUERY 9: Test account detection
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QA CHECK 4: Test/dummy accounts")
print("=" * 50)

cursor.execute("""
    SELECT * FROM users
    WHERE LOWER(name) IN ('admin', 'test', 'dummy', 'guest')
    OR email LIKE '%test%'
    OR email LIKE '%dummy%'
""")
rows = cursor.fetchall()
if rows:
    print(f"❌ BUG: Found {len(rows)} test account(s):")
    for row in rows:
        print(row)
else:
    print("✅ No test accounts found")


# ─────────────────────────────────────────
# QUERY 10: HAVING — filter grouped results
# Different from WHERE — filters GROUPS
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("QUERY 10: Users with more than 1 order")
print("=" * 50)

cursor.execute("""
    SELECT u.name, COUNT(o.id) as order_count
    FROM users u
    JOIN orders o ON u.id = o.user_id
    GROUP BY u.name
    HAVING COUNT(o.id) > 1
""")
for row in cursor.fetchall():
    print(f"{row[0]} has {row[1]} orders")


# ─────────────────────────────────────────
conn.close()
print("\n✅ Day 4 Complete!")