import mysql.connector
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from preference import preference

def create_table(db_name, table_name):
    mydb = mysql.connector.connect(
      host = "localhost",
      user = preference.user,
      passwd= preference.passwd,
      database = db_name
    )

    mycursor = mydb.cursor()

    query = "CREATE TABLE " + table_name + " (sno int(11) PRIMARY KEY, province VARCHAR(255), street VARCHAR(255), dispensary VARCHAR(255), tel VARCHAR(255))"
    mycursor.execute(query)
    
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
