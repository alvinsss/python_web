# -*- coding: utf-8 -*- 
import telnetlib
# '''Telnet远程登录：Windows客户端连接Linux服务�?''
 # 配置选项
Host = '115.28.36.45'  # Telnet服务器IP
username = 'root'  # 登录用户�?
password = 'C6653115c171014'  # 登录密码
finish = ':~$ '  # 命令提示符（标识�?���?��命令已执行完毕）
 
# 连接Telnet服务�?
tn = telnetlib.Telnet(Host, 1000)
 
  # 输入登录用户�?
tn.read_until('login: ')
tn.write(username + '\n')
  
  # 输入登录密码
tn.read_until('Password: ')
tn.write(password + '\n')
  
  # 登录完毕后，执行ls命令
tn.read_until(finish)
tn.write('ls\n')
  
  # ls命令执行完毕后，终止Telnet连接（或输入exit�?���?
tn.read_until(finish)
tn.close()  # tn.write('exit\n')
