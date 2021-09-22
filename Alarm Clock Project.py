from tkinter import *
import datetime  # supplies classes for manipulating dates and times
import time
import pygame

root = Tk()
hour = StringVar()
minute = StringVar()
sec = StringVar()

root.title("Alarm Clock")
root.geometry('300x300')
root_format = Label(root,
                    fg='navy',
                    bg='white',
                    font='Times 15 italic',
                    text='Enter In Time Hour Format!').pack(side=BOTTOM)


def alarm(timer):
    while True:
        time.sleep(1)  # suspend execution for an interval of time
        current = datetime.datetime.now()  # datetime.datetime - a combination of a date and a time
        # .now - returns the current local date and time
        now = current.strftime("%H:%M:%S")  # returns a string representing the date, controlled by an explicit
        # format string. .strftime(format)
        # %H - hours 24-hour
        # %M - minute
        # %S - second
        date = current.strftime("%d/%m/%Y")
        # %d - day
        # %m - month
        # %Y - Year
        print("The date is : ", date)
        print(now)

        if now == timer:
            print("WAKE UP")
            pygame.init()  # .init() - initialize all imported pygame modules
            pygame.mixer.init()
            sound = pygame.mixer.Sound("VoipRing.wav")
            sound.play()
            # winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # .PlaySound(sound, flags)
            # SND_ASYNC - return immediately, allowing sound to play asynchronously
            # works on windows, on mac
            break


def exact():
    exact_time = f"{hour.get()}:{minute.get()}:{sec.get()}"
    alarm(exact_time)


def reset():
    hour.set("")
    minute.set("")
    sec.set("")


def leave():
    root.destroy()


add_time = Label(root,
                 fg='navy',
                 bg='white',
                 font='Times 15 italic',
                 text='Hour Min Sec').place(x=100, y=0)
set_alarm = Label(root,
                  fg='navy',
                  bg='white',
                  font='Times 15 italic',
                  relief='solid',
                  text='Alarm set').place(x=10, y=135)

hourTime = Entry(root,
                 fg='navy',
                 bg='light blue',
                 font='Times 15 italic',
                 textvariable=hour,
                 width=15).place(x=100, y=100)
minuteTime = Entry(root,
                   fg='navy',
                   bg='light blue',
                   font='Times 15 italic',
                   textvariable=minute,
                   width=15).place(x=100, y=135)
secTime = Entry(root,
                fg='navy',
                bg='light blue',
                font='Times 15 italic',
                textvariable=sec,
                width=15).place(x=100, y=170)

submit = Button(root,
                fg='navy',
                bg='light blue',
                font='times 15 italic',
                text='Set Alarm',
                command=exact,
                width=15).place(x=100, y=230)
Button(root,
       font='Times 12 bold',
       fg='navy',
       text='RESET',
       width=6,
       command=reset,
       bg='light blue',
       padx=6,
       pady=2).place(x=10, y=250)

Button(root,
       font='Times 12 bold',
       fg='navy',
       text='EXIT',
       width=6,
       command=leave,
       bg='light blue',
       padx=2,
       pady=2).place(x=250, y=250)

root.mainloop()
