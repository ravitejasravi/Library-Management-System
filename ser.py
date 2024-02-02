import cx_Oracle

con = cx_Oracle.connect("raviteja/raviteja@asus:1521/XE")
print(con.version)

cur = con.cursor()
n = 'jkkkk'
l = 'all'
p = 5

cur.execute(f"""INSERT INTO publisher(name, address, phone) VALUES('{n}', '{l}', {p})""")
con.commit()
print('.')