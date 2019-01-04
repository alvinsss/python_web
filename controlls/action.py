#    -*- coding: utf-8 -*-
'''
Created on Oct 9, 2014
@author: lin
'''
import db.db_conf
import db.mfexchange_sql
import spi.ugc
import spi.env_conf
import spi.sendredpage

def init_mfexchange_user(db_name):
    try:
        db_conn = db.db_conf.get_db(db_name)
        db.mfexchange_sql.init_mfexchange_user(db_conn)
        return  '初始化成功'
    except Exception as e:
        return  '初始化失败：' + str(e)
    
def update_useraddredPage(db_name, userid):
    try:
        http_url = spi.env_conf.get_httpenv(db_name)
        print ('exchange Http'+http_url)
        db_names = db.db_conf.get_db(db_name)
        db_userId = db.mfexchange_sql.select_useridByphone_number(db_names, userid)
        print ('db_name values is:'+db_name)
        print ('http_url values is:'+http_url)
        spi.sendredpage.h_sendredpage(http_url,db_userId)
        return '增加完了！'
    except Exception as e:
        return  '增加失败或用户名不存在：' + str(e)

def update_order_info(db_name, loanId, currentMomey, order_status):
    try:
        db_conn = db.db_conf.get_db(db_name)
        db.mfexchange_sql.update_order_info(db_conn, loanId, currentMomey, order_status)
        return '修改成功！'
    except Exception as e:
        return  '修改失败：' + str(e)
    
def update_user_account(db_name, phone_number, account):
    try:
        db_conn = db.db_conf.get_db(db_name)
        db.mfexchange_sql.update_user_account(db_conn, phone_number, account)
        return '修改成功！'
    except Exception as e:
        return  '修改失败：' + str(e)

def find_phone_numberCode(db_name, phone_number):
    try:
        db_conn = db.db_conf.get_db(db_name)
        message = db.mfexchange_sql.find_phone_numberCode(db_conn, phone_number)
        return message
    except Exception as e:
        return  '没有数据：' + str(e)

# if __name__ == '__main__':
#     update_order_info('11','1','2','3')
#     db_name = db_conf.get_db('beta_1')
#     find_phone_numberCode(db_name,"15811297594")
    
