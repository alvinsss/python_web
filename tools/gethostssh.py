# -*- coding: utf-8 -*-  
#!/usr/bin/python   
import paramiko 
import threading

def ssh2(ip, username, passwd, cmd):  
    try:  
        ssh = paramiko.SSHClient()  
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(ip, 22, username, passwd, timeout=5)  
        for m in cmd:  
            stdin, stdout, stderr = ssh.exec_command(m)  
            stdin.write("Y")  # 交互，输入Y
            out = stdout.readlines()  
            # 屏幕输出  
            for o in out:  
                print o,
        print '%s\tOK\n' % (ip)  
        ssh.close()  
    except :  
        print '%s\tError\n' % (ip)  
        
        
if __name__ == '__main__':
    fpwd = open("keyPwd.txt")
    linepwd = fpwd.readline()
    file_result = open('result.txt', 'a')
    i = 0
    while linepwd:
        i = i + 1 
        cmd = ['cal', 'echo hello!']  # 你要执行的命令列
        username = "root"  # 用户 
#         print linepwd,
#         linepwd = 
        passwd = fpwd.readline()  # 密码
        passwd = 'pass@word1'
        print 'Current username is :%s, pwd is:%s' %(username,passwd)
        threads = [10]  # 多线? 
        file_result.write("print 'Current pwd is:%s' %(passwd)")
        print >> file_result, 'Current pwd is:%s' % (passwd)
        print "Begin......" 
#         for i in range(44,46):  
#             ip = '115.28.36.'+str(i)  
        ip = '192.168.1.23:23'
        sshAction = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))   
        sshAction.start() 
    file_result.close()
    fpwd.close()
