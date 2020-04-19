import schedule
import time
import requests

def job():
    url = 'http://134.122.68.234/api/update/'
    r = requests.post(url)

schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
