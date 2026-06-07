import sqlite3

conn = sqlite3.connect("alta_poc.db")

cursor = conn.cursor()

row = cursor.execute("""
SELECT *
FROM requirements
WHERE id='LOG-001'
""").fetchone()

print("\nID:", row[0])
print("\nTITLE:", row[1])
print("\nCATEGORY:", row[2])
print("\nPRIORITY:", row[3])
print("\nFEATURE:", row[4])
print("\nSCREENS:", row[5])
print("\nPARAMETERS:", row[6])
print("\nRISKS:", row[7])
print("\nDEPENDENCIES:", row[8])

conn.close()