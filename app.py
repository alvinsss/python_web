#    -*- coding: utf-8 -*-
'''
Created on Oct 9, 2014

@author: lin
'''
""" Basic todo list using webpy 0.4 """
import web
import controlls.action

# ## Url mappings

urls = (
    '/index', 'index',
    '/csh', 'csh',
    '/update_user_passwd', 'update_user_passwd',
    '/message', 'message',
    '/update_order_info', 'update_order_info',
    '/update_user_account', 'update_user_account',
    '/find_phone_numberCode', 'find_phone_numberCode',
    '/update_useraddredPage','update_useraddredPage'
)
web.config.debug = True
# ## Templates
render = web.template.render('/static/templates/', base='base')

class index():
    def GET(self):
        return web.seeother('/static/templates/index.html')
        
class csh():
    def POST(self):
        return "init"

    def GET(self):
        name = str(web.input().get('name'))
        # print name.encode()
        message = controlls.action.init_mfexchange_user(name)
        return message
    
class update_user_passwd():
    def GET(self):
        user_id = str(web.input().get('user_id'))
        db_name = str(web.input().get('db_name'))
        # print db_name.encode()
        # print user_id.encode()
        update_user_passwd()
        message = controlls.action.update_user_passwd(db_name, user_id)
        return message

class update_user_account():
    def GET(self):
        phone_number = str(web.input().get('phone_number'))
        account = str(web.input().get('account'))
        db_name = str(web.input().get('db_name'))
        update_user_account()
        message = controlls.action.update_user_account(db_name, phone_number, account)
        return message
    
class update_useraddredPage():
    def GET(self):
        userid = str(web.input().get('user_id'))
        userid = userid.decode('utf-8', 'ignore')
        db_name = str(web.input().get('db_name'))
        db_name = db_name.decode('utf-8', 'ignore')
        print (userid)
        update_useraddredPage()
        #message = controlls.action.update_order_info(db_name, user_id)
        message = controlls.action.update_useraddredPage(db_name, userid)
        return message

class find_phone_numberCode():
    def GET(self):
        phone_number = str(web.input().get('phone_number'))
        db_name = str(web.input().get('db_name'))
        # find_phone_numberCode()
        message = controlls.action.find_phone_numberCode(db_name,phone_number)
        return message

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
