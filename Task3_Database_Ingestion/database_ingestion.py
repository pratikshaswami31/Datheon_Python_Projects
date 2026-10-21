import csv
import sqlite3
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "emp.csv"
DB_FILE = BASE_DIR / "employees.db"

# Connect to SQLite database
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Create employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

# Read CSV and insert or update records
inserted = 0
updated = 0
skipped = 0

try:
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {
            "employee_id", "name", "department", "salary"
        }

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("CSV is missing required columns.")

        for row in reader:
            try:
                employee_id = int(row["employee_id"])
                name = row["name"].strip()
                department = row["department"].strip()
                salary = float(row["salary"])

                if not name or not department or salary < 0:
                    raise ValueError("Invalid employee details.")

                # Check whether employee already exists
                cursor.execute(
                    "SELECT 1 FROM employees WHERE employee_id = ?",
                    (employee_id,)
                )
                exists = cursor.fetchone() is not None

                # Upsert: insert new record or update existing record
                cursor.execute("""
                    INSERT INTO employees
                    (employee_id, name, department, salary)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(employee_id) DO UPDATE SET
                        name = excluded.name,
                        department = excluded.department,
                        salary = excluded.salary
                """, (employee_id, name, department, salary))

                if exists:
                    updated += 1
                else:
                    inserted += 1

            except (ValueError, TypeError):
                skipped += 1
                print("Skipped invalid row:", row)

    connection.commit()

    print("\nDatabase ingestion completed!")
    print("New records inserted:", inserted)
    print("Existing records updated:", updated)
    print("Invalid rows skipped:", skipped)

    # Display final database records
    cursor.execute("""
        SELECT employee_id, name, department, salary
        FROM employees
        ORDER BY employee_id
    """)

    print("\nEmployee Records:")
    for employee in cursor.fetchall():
        print(employee)

except (OSError, csv.Error, ValueError, sqlite3.Error) as error:
    connection.rollback()
    print("Ingestion failed:", error)

finally:
    connection.close()