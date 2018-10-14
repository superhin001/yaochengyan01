import unittest
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib.send_email import *
from config.config import *

logging.info("="*25 + "测试开始" + "="*25)
#suite = unittest.defaultTestLoader.discover("./") #自动取根目录下所有test开头的.py去执行
suite = unittest.defaultTestLoader.discover(testcase_path)

f = open(report_file, 'wb') #读取配置文件中路径（不然报告会写入项目路径下）
HTMLTestRunner(stream=f, title="LT_db_unittest", description="添加、绑定加油卡测试报告").run(suite)

send_email(report_file) #读取配置文件中路径
logging.info("邮件已发送")
logging.info("="*25 + "测试结束" + "="*25)