# Alarm Clock Project
### About: 

For this project, I implemented an alarm clock using Python. I used the libraries tkinter, datetime, time and winsound which helped me to build the project using the current date and time as well as to provide a user interface to set the alarm according to a 24-hour format.

### Results:

First, I created the alarm loop. The loop will initially let the user know what the current time is.  

```python
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
```

Then let the user set his alarm. When the alarm equals the current time, a message will be displayed onto the terminal and a sound will be played.   

```python
def exact():
    exact_time = f"{hour.get()}:{minute.get()}:{sec.get()}"
    alarm(exact_time)
```

This is possible because I set the variable to accept input of strings.

```python
hour = StringVar()
minute = StringVar()
sec = StringVar()
``` 
 
In addition, I set an exit and reset condition for the GUI application.
 
```python
def reset():
    hour.set("")
    minute.set("")
    sec.set("")


def leave():
    root.destroy()
```
 
Afterwards, I created the GUI (graphic user interface) so the user can interact with the code above.

**Sets the title and dimensions of the UI application**

```python
root.title("Alarm Clock")
root.geometry('300x300')
root_format = Label(root,
                    fg='navy',
                    bg='white',
                    font='Times 15 italic',
                    text='Enter In Time Hour Format!').pack(side=BOTTOM)

```

**Sets the words seen on the application as well as provides the area to place inputs in**

```python
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
```

**Sets the buttons the user can press**

```python
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
```

Finally, I closed the mainloop which is the last command given to compile all the previous commands and displays the window as soon as the program is running.

### Final Product:

<img width="296" alt="Screen Shot 2021-09-24 at 4 54 37 PM" src="https://user-images.githubusercontent.com/89553126/134743628-5cb42daf-9723-4f57-b567-e96cd419fbec.png">

***With numeric inputs***

<img width="296" alt="Screen Shot 2021-09-24 at 4 55 48 PM" src="https://user-images.githubusercontent.com/89553126/134743786-6afdbe6a-745f-40e4-b429-2ac0921d333a.png">
 
