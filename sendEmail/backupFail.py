import Index
import datetime

context = f'''
    <div>workApplication DB  備份失敗</div>
    <div>時間 : {datetime.datetime.now()} </div>
'''

Index.send("za96346@gmail.com", context)