import sqlite3

conn = sqlite3.connect('emaildb.sqlite')  # it will create a file with that name since we don't have that file
cur = conn.cursor()  # cursor is kind of like the handle

cur.execute('''
DROP TABLE IF EXISTS Counts''')  # if there is already a table named 'counts', then we drop it and create a new one

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')  # create a table with columns email and count

fname = input('Enter file name')
if (len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    else:
        pieces = line.split()
        email = pieces[1]
        cur.execute('SELECT count FROM Counts WHERE email = ?',(email,))
        #  当开启游标功能执行execute后，系统会将上述得到的匹配行结果，找个地方存储起来，并提供一个游标接口给我们。当需要获取数据的时候，就可以从中拿数据。
        row = cur.fetchone()
        #  cur.fetchone()每执行一次，相当于提取游标当前位置的数据，然后将游标下移一行。但因为这里的目标是验证匹配行结果是否为空，并且count是计数，
        #  所以cur.execute得到的匹配行结果至多只有一行，那就是对应email已经出现的次数。
        if row is None:
            cur.execute('''INSERT INTO Counts (email, count) VALUES(?,1)''',(email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
        conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#  Descending降序排列，只取top 10

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()