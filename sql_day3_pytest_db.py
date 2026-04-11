# sql_day3_pytest_db.py
# Week 6 - SQL for QA Engineers
# Day 3: SQL + PyTest together

import sqlite3
import pytest

# ─────────────────────────────────────────
# DATABASE SETUP
# One shared DB for all tests in this file
# ─────────────────────────────────────────

DB_NAME = "test_qa_day3.db"

def create_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_NAME)
    return conn


def setup_database():
    """Create fresh table with test data."""
    conn = create_connection()
    cursor = conn.cursor()

    # Fresh start every run
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

    # Insert test data
    test_users = [
        ('Rama',   'rama@gmail.com',       22, 1),
        ('Priya',  'priya@gmail.com',      25, 0),
        ('Ravi',   'ravi@gmail.com',       17, 0),
        ('Admin',  'admin@highscores.ai',  30, 1),
        ('Kumar',  'kumar@gmail.com',      28, 0),
    ]

    cursor.executemany("""
        INSERT INTO users (name, email, age, is_paid)
        VALUES (?, ?, ?, ?)
    """, test_users)

    conn.commit()
    conn.close()


# ─────────────────────────────────────────
# PYTEST FIXTURE
# Runs setup once, gives each test
# a fresh connection
# ─────────────────────────────────────────

@pytest.fixture(scope="module")
def db():
    """Setup DB once for all tests in this file."""
    setup_database()
    conn = create_connection()
    yield conn        # tests run here
    conn.close()      # cleanup after all tests done
    print("\n✅ DB connection closed after all tests")


# ─────────────────────────────────────────
# TEST 1: Check total user count
# ─────────────────────────────────────────

def test_total_users(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    assert count == 5, f"Expected 5 users, got {count}"
    print(f"\n✅ Total users: {count}")


# ─────────────────────────────────────────
# TEST 2: Check paid users count
# ─────────────────────────────────────────

def test_paid_users_count(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE is_paid = 1")
    count = cursor.fetchone()[0]
    assert count == 2, f"Expected 2 paid users, got {count}"
    print(f"\n✅ Paid users: {count}")


# ─────────────────────────────────────────
# TEST 3: QA CHECK — no underage users
# Same bug you found on HighScores.ai!
# ─────────────────────────────────────────

def test_no_underage_users(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE age < 18")
    rows = cursor.fetchall()
    assert len(rows) == 0, \
        f"BUG: Found {len(rows)} underage user(s): {rows}"
    print("\n✅ No underage users found")


# ─────────────────────────────────────────
# TEST 4: Specific user exists
# ─────────────────────────────────────────

def test_user_rama_exists(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE email = 'rama@gmail.com'
    """)
    user = cursor.fetchone()
    assert user is not None, "User rama@gmail.com not found in DB"
    assert user[1] == 'Rama', f"Expected name Rama, got {user[1]}"
    print(f"\n✅ User found: {user}")


# ─────────────────────────────────────────
# TEST 5: No empty emails
# Real QA check — email can't be blank
# ─────────────────────────────────────────

def test_no_empty_emails(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM users
        WHERE email IS NULL OR email = ''
    """)
    rows = cursor.fetchall()
    assert len(rows) == 0, \
        f"BUG: Found {len(rows)} users with empty email"
    print("\n✅ All users have valid emails")


# ─────────────────────────────────────────
# TEST 6: UPDATE and verify
# Simulate user upgrading to paid plan
# ─────────────────────────────────────────

def test_update_user_to_paid(db):
    cursor = db.cursor()

    # Priya upgrades to paid
    cursor.execute("""
        UPDATE users SET is_paid = 1
        WHERE email = 'priya@gmail.com'
    """)
    db.commit()

    # Verify update worked
    cursor.execute("""
        SELECT is_paid FROM users
        WHERE email = 'priya@gmail.com'
    """)
    result = cursor.fetchone()[0]
    assert result == 1, f"Expected is_paid=1, got {result}"
    print(f"\n✅ Priya updated to paid: {result}")


# ─────────────────────────────────────────
# TEST 7: No suspicious test emails
# Real QA check for production databases
# ─────────────────────────────────────────

def test_no_test_emails(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM users
        WHERE email LIKE '%test%'
        OR email LIKE '%dummy%'
        OR email LIKE '%fake%'
    """)
    rows = cursor.fetchall()
    assert len(rows) == 0, \
        f"BUG: Found suspicious emails: {rows}"
    print("\n✅ No test/dummy emails found")