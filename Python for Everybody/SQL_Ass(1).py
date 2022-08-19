import sqlite3

conn = sqlite3.connect('sql_ass1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open('C:\\Users\\asus\\Desktop\\mbox.txt')
for line in fh:
    if not line.startswith('From: '):
        continue
    else:
        pieces_1 = line.split()
        pieces_2 = pieces_1[1].split('@')
        domain = pieces_2[1]
        cur.execute('SELECT count FROM Counts WHERE org = ?',(domain,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)',(domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(domain,))
        conn.commit()

cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')
for k in cur:
    print(str(k[0]),k[1])
cur.close()