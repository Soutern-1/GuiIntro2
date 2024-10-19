from tkinter import *


if __name__ == "__main__":

    gui = Tk()

    gui.geometry("200x200")

    gui.config(background="black")

    gui.title("Calender")

    cal = Label(gui, text = "Calendar", bg= "dark gray", font=("times new roman",28,"bold"))

    cal.grid(row = 3, column=3)

    gui.mainloop()
