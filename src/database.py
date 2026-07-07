import pyodbc

SERVER = r'JARUGU\SQLEXPRESS'
DATABASE = 'CustomerChurnDB'

try:
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'Trusted_Connection=yes;'
    )

    print("✅ Connected Successfully!")

except Exception as e:
    print("Connection Failed")
    print(e)