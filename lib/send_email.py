import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import *
def send_email(report_file):
    #编写邮件正文
    with open(report_file, 'rb') as f:
        email_body = f.read()
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body, 'html', 'utf-8')) #添加html邮件正文 #不写utf-8 不能正确显示中文
    #组装邮件头
    msg['From'] =smtp_user
    msg['To'] = receiver
    msg['Subject'] = '邮件主题-接口测试报告'
    #3、构造附件
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="report.html"'
    msg.attach(att1)
    #4、连接smtp服务器并发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user, smtp_password)
        smtp.sendmail(smtp_user, receiver, msg.as_string())
    except Exception as e:
        print(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email(report_file)