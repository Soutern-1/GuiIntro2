from tkinter import *


def openWindow():

    calendar = Tk()

    calendar.geometry("1000x1000")

    calendar.config(background="white")

    calendar.title(f"Calendar of year {int(enteryear.get())}")

    calendar.calendar(int(enteryear.get()))


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



