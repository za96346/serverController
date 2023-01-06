from sendEmail import send
import datetime

context = f'''
    <div>workApplication DB  備份成功</div>
    <div>時間 : {datetime.datetime.now()} </div>
'''

send("za96346@gmail.com", context)