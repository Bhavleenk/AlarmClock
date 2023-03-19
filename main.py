from tkinter import * #used for GUI
import datetime
import time
import winsound #for sound of alarm

def alarm(SetAlarmTimer):
  while True:
    CurrentTime=datetime.datetime.now()
    now=CurrentTime.strftime("%H:%M:%S")
    date = CurrentTime.strftime("%d/%m/%Y") #string conversion using strftime
    print("The set Date is : ", date)
    print(now)
    if now==SetAlarmTimer:
      print("Time to Wake Up!")
      winsound.Playsound("sound.wav", winsound.SND_ASYNC)
      break

