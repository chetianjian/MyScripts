import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb1.sqlite')
cur = conn.cursor()

#Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

fname = 'C:\\Users\\asus\\Desktop\\code3\\tracks\\Library.xml'
if (len(fname)<1):
    fname = 'Library.xml'

# 这个函数的逻辑是，found初始值为False，则if found为if False则不会执行，直到d中出现一个child，使得child的tag的属性为键，并且child的内容为
# 函数中输入的key值，found才变更为True。而一旦found变为True，在下一次循环中，if found为if True，则执行，return child的内容后函数结束，而
# 不会执行最后的return None。当且仅当found不曾变为True，也就是第二个条件语句不曾执行时，才会执行最后的return None，即函数的返回结果为None。
def lookup(d,key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:',len(all))


# all为xml文件中所有dict/dict/dict的tag的序列，对于其中每一项entry，求先前定义的函数lookup(entry,'Track ID')的返回值，若返回为None，
# 说明此entry中的所有的子tag的性质都不为‘键’或值都不为‘Track ID’，因此可以跳过。但若存在Track ID的tag，再通过lookup函数找到每一个entry
# 对应的name、artist、album等值。当name或artist或album任意一值缺失时，跳过循环。若三个全齐，则print name、artist等信息。
for entry in all:
    if (lookup(entry,'Track ID') is None):
        continue
    else:
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')

        if name is None or artist is None or album is None:
            continue
        else:
            print(name, artist, album, count, rating, length)

        # 在创建Artist Table的时候，name定义为UNIQUE，因此如果出现相同的name，程序会出错。因此此处的INSERT OR IGNORE的意思是，如果已经
        # 存在这个名字，就不要重复INSERT了
        cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''' ,(artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title,artist_id) VALUES(?,?)''',(album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
        album_id = cur.fetchone()[0]

        # 和IGNORE相似，如果违反了UNIQUE，则REPLACE的作用相当于UPDATE
        cur.execute('''INSERT OR REPLACE INTO Track 
        (title, album_id, len, rating, count) VALUES(?,?,?,?,?)''',(name, album_id, length, rating, count))
        conn.commit()