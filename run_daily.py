import schedule
import time as tm
import scrape_opel_fr

schedule.every().day.at("10:00").do(scrape_opel_fr.scrape())

while True:
    schedule.run_pending()
    tm.sleep(1)