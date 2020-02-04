from urllib.request import urlopen
from urllib.request import urlretrieve
import urllib.request

from bs4 import BeautifulSoup
import ssl
import os
import pymysql
import time
from datetime import datetime
from preference import preference
from mySqlService import mySqlService

def makeDir(name):
    try:
        mydir = "./download/" + name
        if not(os.path.isdir(mydir)):
            print("make dir")
            os.makedirs(os.path.join(mydir))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("failed to create dir")
            raise

def crawling():
    sqlService = mySqlService()

    #con = pymysql.connect(host=preference.host, user=preference.user, password=preference.passwd, db=preference.db_name, charset='utf8')
    #cur = con.cursor()

    while True:
        print('@@@ start crawling dispensary @@@')
        sqlService.deleteAllRow()
        try:
            context = ssl._create_unverified_context()
            request = urllib.request.Request(preference.crawling_url)

            with urlopen(request, context=context) as response:
                soup = BeautifulSoup(response, 'html.parser')
                size = 0
                sno = 0

                for tr in soup.find_all('tr'):
                    try:
                        if(tr.find('th',{'scope': 'row'}) != None):
                            list = tr.find_all('td')

                            province = list[0].text
                            street = list[1].text
                            dispensary = list[2].text
                            tel = list[3].text

                            sqlService.insert(sno, province, street, dispensary, tel)
                            sno += 1

                            #sql = """insert into dispensary(sno,subject,author,link,regdate,recomm,viewcount) values (%s, %s, %s, %s, %s, %s, %s)"""
                            #cur.execute(sql, (sno, province, street, dispensary, tel))
                            #con.commit()

                            '''
                            print('1 %s'%(list[0].text))
                            print('2 %s'%(list[1].text))
                            print('3 %s'%(list[2].text))
                            print('4 %s'%(list[3].text))
                            '''


                    except Exception as e:
                        print("=========== Errror %s ==========="%e)
                        continue
                    finally:
                        size += 1

                print('dispensary size %d'%size)
        except Exception as e:
            print("=========== Errror %s ==========="%e)
            continue
        time.sleep(60*60*24)

if __name__ == "__main__":
    crawling()
    #sqlService = mySqlService()
    #sqlService.deleteAllRow()
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

