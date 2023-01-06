import os
import smtplib
from dotenv import load_dotenv
import email
import datetime

load_dotenv()
key = os.getenv('EMAIL_AUTH_TOKEN')
mailForm = os.getenv('EMAIL_ACCOUNT')

def send(toEmail, context):
    msg = email.message.EmailMessage()
    msg['From']="workApp"
    msg['To']=toEmail#"收件人"
    msg['Subject']="資料寫入"

    #寄送比較多的內容
    msg.add_alternative(
        f'''
            <div>workApplication DB  備份成功</div>
            <div>時間 : {datetime.datetime.now()} </div>
            {context}
        ''',
        subtype="html"
    )
    #連線到smtp server

    #可以到網路上收尋
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(mailForm, key)#("帳號","密碼")
    server.send_message(msg)
    server.close()
if __name__=="__main__":
    send("za96346@gmail.com", "")
    
