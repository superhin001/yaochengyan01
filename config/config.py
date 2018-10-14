import os
import logging
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = os.path.join(prj_path, 'data', 'data_fuel.xlsx') #设置路径，然后read_excel 中导入配置包就能找到这个文件
report_file = os.path.join(prj_path, 'report', 'report.html')

log_file = os.path.join(prj_path, 'log', 'log.txt')
testcase_path = os.path.join(prj_path, 'test_case_file')


#日志
logging.basicConfig(level=logging.INFO, #log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)s] %(message)s)',
                    datefmt='%Y-%m-%d %H:%M:%S',#日期格式
                    #filename='log.txt', #运行后在当前目录下生成log.txt(然后配置路径就可以输出到指定文件夹里了)
                    filename=log_file,
                    filemode='a') #追加模式
#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'longtengserver'

#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '18247108537@163.com'
smtp_password = 'ycy315421'

sender = smtp_user
receiver = '765049184@qq.com'
Subject = '接口测试报告'
#email_body = 'hi all 测试完成，请查看附件'  这里暂不使用，使用的是report.html 添加到了正文中

if __name__ == '__main__':
    logging.info('hello')  #运行后在当前目录下生成log.txt

