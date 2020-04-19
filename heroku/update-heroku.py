import schedule
import time
import requests

def job():
    url = 'https://worldometer-scrapper.herokuapp.com/api/update/'
    print("send data to heroku")    
    files = {'file': open('/root/worldometer/dataset/wworldometer.csv', 'rb')}
    r = requests.post(url, files=files)

schedule.every().day.at("16:40").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
