import sqlite3
 
 
def main():
    try:
        con = sqlite3.connect('/home/mec/mec_database.db')
        cur = con.cursor()
        cur.executescript('''DROP TABLE IF EXISTS CacheTable;
            CREATE TABLE CacheTable(Host_ip varchar(16), cpu int(3), memory int(3), storage int(3));
            INSERT INTO CacheTable (Host_ip, cpu, memory, storage) VALUES('192.168.1.1', '20', '11, '15');
            INSERT INTO CacheTable (Host_ip, cpu, memory, storage) VALUES('192.168.1.2', '22', '13, '16');''')
 
        con.commit()
 
        cur.execute("SELECT * FROM CacheTable")
 
        data = cur.fetchall()
 
        for row in data:
            print(row)
 
    except sqlite3.Error as e:
        if con:
            con.rollback()
            print('Error Encountered: {}'.format(e))
 
    finally:
        if con:
            con.close()
 
 
if __name__ == "__main__":
    main()
