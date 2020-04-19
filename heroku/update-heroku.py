import schedule
import time
import requests

def job():
    url = 'http://127.0.0.1:8000/api/update/'
    r = requests.post(url)

schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
