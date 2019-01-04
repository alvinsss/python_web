#    -*- coding: utf-8 -*-
'''
@author: lin
'''
import  pymysql
pymysql.install_as_MySQLdb()

def get_db(db_key):

    if db_key == 'beta_1':
        conn = MySQLdb.connect(host="mham.fengjr.inc", port=3306, user="hailin", passwd="BaW~Lx[ZNUVJS$%k", charset="utf8")
        print ('db link----' + db_key )
        return conn
    
    elif db_key == 'beta_2':
        conn = MySQLdb.connect(host="10.255.73.220", port=3306, user="hailin", passwd="BaW~Lx[ZNUVJS$%k", charset="utf8")
        print ('db link---' + db_key )
        return conn
    
#if __name__ == '__main__':
#    conn = get_db('beta_2')
#    conn.close
    
    
        
        
    
