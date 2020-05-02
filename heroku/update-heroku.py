import schedule
import time
import requests

def job():
    url = 'http://157.230.101.0/api/update/'
    r = requests.post(url)

schedule.every().day.at("18:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
