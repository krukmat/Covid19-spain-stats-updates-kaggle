import schedule
import time
import urllib2
import csv 
import kaggle
import subprocess

def job():
    print("Extract data")    
    subprocess.call(['scrapy', 'crawl', 'worldometer', '-o', '/root/worldometer/dataset/wworldometer.csv','-t','csv'])
    subprocess.call(['kaggle', 'datasets', 'version', '-p', '/root/worldometer/dataset/', '-m', 'new version'])

schedule.every().day.at("18:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
