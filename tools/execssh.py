#!/usr/bin/python
 #-*- coding: utf-8 -*-
import paramiko 
 #paramiko.util.log_to_file('/tmp/sshout')
def ssh2(ip,username,passwd,cmd):
     try:
         ssh = paramiko.SSHClient()
         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         ssh.connect(ip,22,username,passwd,timeout=5)
         stdin,stdout,stderr = ssh.exec_command(cmd)
 #           stdin.write("Y")   #简单交互，输入 ‘Y’
         print stdout.read()
 #        for x in  stdout.readlines():
 #          print x.strip("＼n")
         print '%s Login is OK '%(ip)
         ssh.close()
     except :
         print '%s Login is Error '%(ip)
if __name__ == '__main__':
       
#  ssh2("192.168.1.23","root","pass@word1","hostname;ifconfig")
    fpwd = open("keyPwd.txt")
    linepwd = fpwd.readline()
    file_result = open('result.txt', 'a')
    i = 0
    while linepwd:
        i = i + 1 
#         cmd = ['cal', 'echo hello!']  # 你要执行的命令列
        username = "alvin"  # 用户 
        passwd = fpwd.readline()  # 密码
        print "Begin......" 
#         for i in range(44,46):  
#             ip = '115.28.36.'+str(i)  
        ssh2("192.168.1.23",username,passwd,"hostname;ifconfig")
#         ssh2("192.168.1.23","root","pass@word1","hostname;ifconfig")
        print 'Current username is :%s, pwd is:%s' %(username,passwd)
        file_result.write("print 'Current pwd is:%s' %(passwd)")
        print >> file_result, 'Current pwd is:%s' % (passwd)
        print "End......" 

    file_result.close()
    fpwd.close()



