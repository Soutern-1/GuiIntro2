from tkinter import *
import calendar


def openWindow():

    calendarWindow = Tk()

    calendarWindow.geometry("1000x1000")

    calendarWindow.config(background="white")

    calendarWindow.title(f"Calendar of year {int(enteryear.get())}")

    calendar_text = calendarWindow.calendar(int(enteryear.get()))

    cal_year = Label(calendarWindow, text=calendar_text, font="Times New Roman 10 bold")

    cal_year.grid(row=1,column=1, padx=30, pady=30)

    calendarWindow.mainloop()


if __name__ == "__main__":

    gui = Tk()

    gui.geometry("500x500")

    gui.config(background="black")

    gui.title("Calendar")

    cal = Label(gui, text = "Calendar", bg= "dark gray", font=("times new roman",22,"bold"))

    cal.grid(row = 1, column=1, padx=30,pady=5)

    info = Label(gui, text = "Enter a year below to view the calendar", bg= "dark gray", font=("times new roman",14,"bold"))
    info.grid(row = 2, column=1, pady=5)


    enteryear = Entry(gui, background="white" ) 
    enteryear.grid(row = 3, column=1, padx=30,pady=10)

    confirm = Button(gui, text = "Confirm Year", bg= "dark gray", font=("times new roman",14,"bold" ), command = openWindow)
    confirm.grid(row=4,column=1,pady=10, )

    exit = Button(gui, text = "Exit", bg= "dark gray", font=("times new roman",14,"bold"), command=exit)
    exit.grid(row=5, column=1, pady=10)
    gui.mainloop()

    enterededyear = int(enteryear.get())





