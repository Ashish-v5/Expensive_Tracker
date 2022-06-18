
import sqlite3
conn=sqlite3.connect("ExpenseTracker.db")
cursor = conn.execute("SELECT * from Expense")
for row in cursor:
    print(row)
cursor = conn.execute("SELECT * from User")
for row in cursor:
    print(row)
cursor = conn.execute("SELECT * from Budget")
for row in cursor:
    print(row)
conn.close()