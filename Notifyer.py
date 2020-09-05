import schedule
import time

from win10toast import ToastNotifier


def notify():
  
    toaster = ToastNotifier()
    toaster.show_toast("DINNER","come for dinner  TANMAY",duration=10)

#scheduler 
schedule.every().day.at("12:00").do(notify)



while True:
    schedule.run_pending()
    time.sleep(1)
   

