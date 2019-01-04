#    -*- coding: utf-8 -*-
'''
Created on Oct 9, 2013
@author: lin
'''

import  pymysql
pymysql.install_as_MySQLdb()
import  db.db_conf

def init_mfexchange_user(conn):
    
    sql1 = "UPDATE users set phone_number=user_id;"
    cursor = conn.cursor()
    conn.select_db("mfexchange")
    cursor.execute(sql1)
    conn.commit()
    
    sql2 = "UPDATE mis_users set phone_number=user_id;"
    cursor = conn.cursor()
    conn.select_db("mfexchange")
    cursor.execute(sql2)
    conn.commit()
    
    sql3 = "UPDATE users set realName=substr(realName,1,2)  WHERE LENGTH(realName) > 6;"
    print (sql3)
    cursor = conn.cursor()
    conn.select_db("mfexchange")
    cursor.execute(sql3)
    conn.commit()
     
#     sql4 = "UPDATE users set realName=concat (realName,'微')  WHERE LENGTH(realName) > 3;"
#     print sql4
#     cursor = conn.cursor()
#     conn.select_db("mfexchange")
#     cursor.execute(sql4)
#     conn.commit()
# 
#     sql5 = "UPDATE users set realName=concat (realName,'微')  WHERE LENGTH(realName) > 3;"
#     print sql5
#     cursor = conn.cursor()
#     conn.select_db("mfexchange")
#     cursor.execute(sql5)
#     conn.commit()
    
    sql6 = "UPDATE  users set phone_number=15811297594 , password='1b94d3fef4fc0a7b5707b761e7fbd74b8e0ebfaf14caa013c9c763ff02f85552'  WHERE  user_id='2335';"
    cursor = conn.cursor()
    conn.select_db("mfexchange")
    cursor.execute(sql6)
    conn.commit()
    
    sql7 = "UPDATE  users set  phone_number=13611293208 ,password='fcbdf647ea2ae6bff9c859e0403cd219648349d27e11d9fc0304c0d681538eb4' WHERE  user_id='3618';"
    cursor = conn.cursor()
    conn.select_db("mfexchange")
    cursor.execute(sql7)
    conn.close()
    conn.commit()
    
    # update_user_passwd 
def update_user_passwd(db_name, user_id):
    sql = "UPDATE  users set username='weijinsuo',`password`='43cc73be1e0389f978b0142f61798dc93a54b2eb44df61b59892aec37814135a'  WHERE  user_id=\'" + user_id + "\' or phone_number=\'" + user_id + "\';"
#     sql2 = "insert ignore into security_resource_mapping(username, resource_id) select \'"+name+"\' ,_group from (select distinct(_group) as _group from resource where _group != '') as a"
#     sql3 = "insert ignore into security_mapping(username, data_id) select \'"+name+"\', id from resource where _group in (select distinct(resource_id) from security_resource_mapping where username =\'"+name+"\')".format(name,name)
    print (sql)
    cursor = db_name.cursor()
    db_name.select_db("mfexchange")
    ru = cursor.execute(sql)
    db_name.commit()
    if (ru > 0) == True:
        return "修改成功"
    return "修改失败"    

def update_order_info(db_conn, loanId, currentMomey, order_status):
    sql = "update loan set currentMomey='" + currentMomey + "'  , `status`='" + order_status + "' WHERE loan_id='" + loanId + "'"
    cursor = db_conn.cursor()
    db_conn.select_db("mfexchange")
    cursor.execute(sql)
    db_conn.commit()
    cursor.close()
    db_conn.close()
    return "修改成功"

def select_useridByphone_number(db_conn, userid):
    id = 'null'
    sql = "SELECT id from TB_USER  WHERE LOGINNAME='"+ userid +"'"
    cursor = db_conn.cursor()
    db_conn.select_db("Biz")
    cursor.execute(sql)
    db_conn.commit()
    res = cursor.fetchone()
    id = res[0]
    print ('userid db values is:'+id)
    return id


def update_user_account(db_conn, phone_number, account):
    
    sql = "SELECT user_id from users WHERE user_id='" + phone_number + "' or phone_number='" + phone_number + "'"
    cursor = db_conn.cursor()
    db_conn.select_db("mfexchange")
    cursor.execute(sql)
    db_conn.commit()
    res = cursor.fetchone()
    userId = res[0]
#     print userId
#     print account
#     print type(userId)
#     print type(account)
    sqlacountBalance = "SELECT acountBalance from account WHERE userid='" + str(userId) + "'"
    cursor = db_conn.cursor()
    db_conn.select_db("mfexchange")
    cursor.execute(sqlacountBalance)
    db_conn.commit()
    res1 = cursor.fetchone()
    acountBalance = res1[0]
    print (acountBalance0)
    
    
    sqlavailableFunds = "SELECT acountBalance from account WHERE userid='" + str(userId) + "'"
    cursor = db_conn.cursor()
    db_conn.select_db("mfexchange")
    cursor.execute(sqlavailableFunds)
    db_conn.commit()
    res2 = cursor.fetchone()
    availableFunds = res2[0]

    sql1 = "UPDATE account a set a.acountBalance=a.acountBalance+'" + account + "',a.availableFunds=a.availableFunds+'" + account + "' WHERE userid = '" + str(userId) + "'"
    cursor = db_conn.cursor()
    db_conn.query("set names 'utf8'")
    db_conn.select_db("mfexchange")
    cursor.execute(sql1)
    db_conn.commit()
    
    sql2 = "INSERT INTO `account_log` (`userid`,`to_userid`,`orderid`,`status`,`type`,`total`,`addtime`,`adduser`,`remark`,`currency`,`source_account`,`dest_account`,`availableFound`,`accountBalance`)  VALUES ('" + str(userId) + "', 0, ROUND(ROUND(RAND(),16)*10000000000000000), 'yes', 'chongzhi', '" + account + "', NOW(), 2335, '充值', 'RMB', NULL, NULL, '" + str(availableFunds) + "'+'" + account + "', '" + str(acountBalance) + "'+'" + account + "')"
    cursor = db_conn.cursor()
    db_conn.select_db("mfexchange")
    ru_i = cursor.execute(sql2)
    db_conn.commit()
    cursor.close()
    db_conn.close()
    if (ru_i > 0) == True:
        return "机号码或UserId不存在"  
    return "增加成功"

def find_phone_numberCode(db_conn, phone_number):
    try:
        smsContext = 'null'
        sql = "SELECT actual_msg as smsContext from sms_record WHERE mobileNum='" + phone_number + "' ORDER BY id desc LIMIT 1"
        print (sql)
        cursor = db_conn.cursor()
        db_conn.select_db("smsgateway")
        cursor.execute(sql)
        db_conn.commit()
        res = cursor.fetchone()
        smsContext = res[0]
        print (smsContext)
#         print smsContext[4:]
        return smsContext
        cursor.close
        db_conn.close
#         mail = ""
#         for message in messagelist:
#             mail = mail + message
#         web.config.smtp_server = 'mail.corp.qunar.com'
#         web.sendmail('ots_beta@qunar.com', 'ots_beta@qunar.com', ota_message, mail)
    except Exception as e:
        print (e)
        return '数据库没有短信！' 
    finally:
        cursor.close
        db_conn.close


if __name__ == "__main__":

    db_conn = db_conf.get_db('beta_1')
#     find_phone_numberCode(db_conn,"15811297594")
    
    
