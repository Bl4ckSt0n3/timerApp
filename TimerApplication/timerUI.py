import time
from tkinter import *
from tkinter import messagebox

_stop = True
class TimerCountdown:

    def __init__(self, master):
        super().__init__()
        self.initUI(master)
    
    def initUI(self, master):

        self.master = master
        master.geometry("480x300")
        master.title("timer")

        self.frame = Frame(master)
        self.frame.pack(fill=BOTH, expand=True)

        self.hour = StringVar()
        self.hour.set("00")

        self.minute = StringVar()
        self.minute.set("00")

        self.second = StringVar()
        self.second.set("00")

        self.entryHour = Entry(self.frame, width=4, textvariable=self.hour, font=("verdana 30"))
        self.entryHour.place(x=100, y=60)

        self.entryMinute = Entry(self.frame, width=4, textvariable=self.minute, font=("verdana 30"))
        self.entryMinute.place(x=190, y=60)

        self.entrySecond = Entry(self.frame, width=4, textvariable=self.second, font=("verdana 30"))
        self.entrySecond.place(x=280, y=60)

        self.button = Button(self.frame, text="countdown", width=9, bd=4, command=self.countdown)
        self.button.place(x=200, y=140)

        self.button_stop = Button(self.frame, text="stop", width=9, bd=4, command=self.stop)
        self.button_stop.place(x=120, y=140)

        self.button_start = Button(self.frame, text="start", width=9, bd=4, command=self.start)
        self.button_start.place(x=280, y=140)

        self.lblHour = StringVar()
        self.lblHour.set("--")
        self.labelHour = Label(self.frame, textvariable=self.lblHour, font=("verdana 30"))
        self.labelHour.place(x=160, y=200)

        self.lblMinute = StringVar()
        self.lblMinute.set("--")
        self.labelMinute = Label(self.frame, textvariable=self.lblMinute, font=("verdana 30"))
        self.labelMinute.place(x=210, y=200)

        self.lblSecond = StringVar()
        self.lblSecond.set("--")
        self.labelSecond = Label(self.frame, textvariable=self.lblSecond, font=("verdana 30"))
        self.labelSecond.place(x=260, y=200)

    def countdown(self):
        
        try:
            self.get_time = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.second.get())

        except:
            messagebox.showinfo("Invalid Value", "Please input valid value!")

         
        while self.get_time > -1:

            self.hrs = 0
            self.mnts = self.get_time // 60
            self.secs = self.get_time % 60

            if self.mnts > 60:

                self.hrs = self.mnts // 60
                self.mnts = self.mnts % 60
            
            self.lblHour.set("{0:2d}".format(self.hrs))
            self.lblMinute.set("{0:2d}".format(self.mnts))
            self.lblSecond.set("{0:2d}".format(self.secs))

            if not _stop:
                return

            tk.update()
            time.sleep(1)

            if self.get_time == 0:
                messagebox.showinfo("Timer", "Time is over !")

            self.get_time -= 1
       

    def stop(self):

        global _stop
        _stop = False

    def start(self):

        global _stop
        _stop = True

        self.get_time = int(self.labelHour['text']) * 3600 + int(self.labelMinute['text']) * 60 + int(self.labelSecond['text'])

        while self.get_time > -1:

            self.hrs = 0
            self.mnts = self.get_time // 60
            self.secs = self.get_time % 60

            if self.mnts > 60:

                self.hrs = self.mnts // 60
                self.mnts = self.mnts % 60
            
            self.lblHour.set("{0:2d}".format(self.hrs))
            self.lblMinute.set("{0:2d}".format(self.mnts))
            self.lblSecond.set("{0:2d}".format(self.secs))

            if not _stop:
                return

            tk.update()
            time.sleep(1)

            if self.get_time == 0:
                messagebox.showinfo("Timer", "Time is over !")

            self.get_time -= 1


tk = Tk()
tk.resizable(False, False)
TimerApp = TimerCountdown(tk)
tk.mainloop()




