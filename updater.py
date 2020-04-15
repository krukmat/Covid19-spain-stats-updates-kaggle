import schedule
import time
import urllib2
import csv 
import kaggle
import subprocess

def update_data():
    response = urllib2.urlopen('https://covid19.isciii.es/resources/serie_historica_acumulados.csv')
    cr = csv.reader(response)
    data = list(cr)
    writer = csv.writer(open("/root/dataset/dataset.csv", 'w'))
    for row in data:
        writer.writerow(row)
        if len(row) == 0:
            break
def job():
    print("Extract data")
    update_data()
    subprocess.call(['kaggle', 'datasets', 'version', '-p', '/root/dataset/', '-m', 'new version'])

schedule.every().day.at("15:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
