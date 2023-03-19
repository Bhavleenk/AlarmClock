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

def ActualTime():
  SetAlarmTimer="{hour.get()}:{min.get()}:{sec.get()}"
  alarm(SetAlarmTimer)


clock = Tk()

clock.title ("Alarm Clock")
clock.geometry("400x200")
TimeFormat=Label(clock, text = "Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=60, y=120)

addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = ActualTime).place(x =110,y=70)
clock.mainloop()




