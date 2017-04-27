import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['facebook.com','www.facebook.com','masrawy.com','www.masrawy.com']
hosts_temp = 'hosts'

while True:
    if dt.now().hour >= 8 and dt.now().hour <=16:
        print("Working Day!")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list :
                if website in content :
                    pass
                else :
                    file.write(redirect+' '+website+'\n')
    else :
        with open(hosts_path,'r+')as file :
            content = file.readlines()
            file.seek(0)
            for line in content :
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('enjoy')
        break
    time.sleep(3)
