# coding=utf-8

import sys
import os
import java
import unittest
import time

# scan_files是在另外�?��地方实现的函数，这里删除了函数的实现方法，是为了大家看单元测试这块清�?
for jar_file in scan_files("F:\Workspaces\QA\AutoTest_WEBUI\libs", postfix=".jar"):
    sys.path.append(jar_file)

print sys.path

from com.mysql.jdbc import Driver
import java.sql.Connection
from java.sql import DriverManager
import org.apache.commons.net.ftp.FTP;
from org.apache.commons.net.ftp import FTPClient
import org.apache.commons.net.ftp.FTPReply


def mysql_driver_test(): 
    java.lang.Class.forName('com.mysql.jdbc.Driver')
    conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/mfexchange", "qa", "qatest");


class FTPClientTest(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        print "starting\n",
        
    def test_login(self):
        ftp = FTPClient()
        ftp.connect("192.168.23.117")
        ftp.login("root", "root")
        self.assertEquals(ftp.getReplyCode(), 230)
    
    def test_files_list(self):
        # 这里之所以重新登录ftp服务器，不重用前面case的结果，就是为了保持各个case的独立�?，确保不�?
        # 因为前面case的原因影响后继的测试
        file_existing = False
        ftp = FTPClient()
        ftp.connect("192.168.23.117")
        ftp.login("root", "root")
        
        if ftp.getReplyCode() == 230:
            files = ftp.listNames("/export/home/test")
            for fi in files:
                if "python-2.5-sol10-x86-local.gz" in fi:
                    file_existing = True
                    break
                
        self.assertEquals(file_existing, True)
        
    def tearDown(self):
        print "cost", time.time() - self.start_time, " second"
        print "end"    

if __name__ == "__main__":
    unittest.main()
