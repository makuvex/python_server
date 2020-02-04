import pymysql
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from preference import preference
import json

class mySqlService:
    
    cur = None
    con = None
    
    def __init__(self):
        #print('__init__')
        self.con = pymysql.connect(host=preference.host, 
                              user=preference.user, 
                              password=preference.passwd, 
                              db=preference.db_name, 
                              charset='utf8')
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()
        
    def insert(self, sno, province, street, dispensary, tel):
        sql = """insert into dispensary(sno, province, street, dispensary, tel) values (%s, %s, %s, %s, %s)"""
        self.cur.execute(sql, (sno, province, street, dispensary, tel))
        self.con.commit()

    def selectAll(self):
        #print('selectLink')
        sql = "select * from " + preference.table_name
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
    def deleteAllRow(self):
        sql = """DELETE FROM dispensary"""
        self.cur.execute(sql)
        self.con.commit()
        
    def selectAllToJson(self):
        sql = "select * from " + preference.table_name
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        
        dispensaryJson = {'status': '200', 'results': None}
        
        if(len(rows) == 0):
            return dispensaryJson
        
        array = []
        i = 0
        for row in rows:
            array.append({'sno': row[0], 
                          'province': row[1],
                          'street': row[2],
                          'dispensary': row[3],
                          'tel': row[4]})
            i += 1

        dispensaryJson = {'status': '200', 'results': array}
        return dispensaryJson
        
        
'''
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| sno        | int(11)      | NO   | PRI | NULL    |       |
| province   | varchar(255) | YES  |     | NULL    |       |
| street     | varchar(255) | YES  |     | NULL    |       |
| dispensary | varchar(255) | YES  |     | NULL    |       |
| tel        | varchar(255) | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+      
'''    

        
        