from tkinter import *

import calendar


def showCal():
    root = Tk()

    root.config(background="white")

    root.title("CALENDAR")
    root.geometry("550x590")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    with open('dates.txt', 'w+') as file:
        file.write(cal_content)

    cal_year = Label(root, text=cal_content, font="Consolas 10 bold")

    cal_year.grid(row=5, column=1, padx=20)

    root.mainloop()


if __name__ == "__main__":
    root = Tk()

    root.config(background="light grey")

    root.title("CALENDAR")

    root.geometry("310x100")

    cal = Label(root, text="CALENDAR", bg='white',
                font=("times", 28, 'bold'), justify=LEFT)

    year = Label(root, text="Enter Year", bg="light grey")

    year_field = Entry(root, bg="white", relief=SUNKEN)

    Show = Button(root, text="Show Calendar", fg="Black",
                  bg="teal", relief=RIDGE, command=showCal)

    Exit = Button(root, text="Exit", fg="Black", bg="teal", relief=RIDGE, command=exit)

    color = Label(bg='white')

    cal.place(x=0, y=0, width=310)

    year.place(x=0, y=50)

    year_field.place(x=60, y=50, height=25)

    Show.place(x=190, y=50)

    Exit.place(x=280, y=50)

    color.place(x=0, y=80, width=310, height=80)

    root.mainloop()