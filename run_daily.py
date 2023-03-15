import schedule
import time
import scrape_opel_fr

def job():
    print(time.strftime("%H:%M:%S", time.localtime()))
    scrape_opel_fr.scrape()

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)