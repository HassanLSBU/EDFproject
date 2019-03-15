import sqlite3
 
 
def main():
    try:
        con = sqlite3.connect('/home/mec/mec_database.db')
        cur = con.cursor()
        cur.executescript('''DROP TABLE IF EXISTS utilTable;
            CREATE TABLE utilTable(Host_ip varchar(16), cpu varchar(3), memory varchar(3), storage varchar(3));
            INSERT INTO utilTable (Host_ip, cpu, memory, storage) VALUES('192.168.1.1', '11', '12', '19');
            INSERT INTO utilTable (Host_ip, cpu, memory, storage) VALUES('192.168.1.2', '21', '22', '29');''')

 
        con.commit()
 
        cur.execute("SELECT * FROM utilTable")
 
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