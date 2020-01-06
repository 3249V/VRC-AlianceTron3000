from tkinter import *
import time
from tkinter.ttk import*
#from LoadingTest import *
root = Tk()
photo = PhotoImage(file = r"C:\Users\Connor\Downloads\settings.png")
bigFrame = Frame(root)
bigFrame.pack(ipadx= 100)
bigFrame2 = Frame(root)
AutonCheck = IntVar()

def rofl(frame2):
    bigFrame.destroy()
    frame2.destroy()
    what = Label(root, text = "Not Finished Yet")
    what.pack(pady = 10)

    checkbox = Checkbutton(root, text = "Show Auton Points", variable = AutonCheck)
    checkbox.pack(padx = 10)

    if AutonCheck == 1:
        checkbox.select()

    idk = Button(root, text="Back", command = lambda :WhyEven(idk, what, ))
    idk.pack(pady = 10)


class WhyEven():
    def __init__(self, t1, t2, t3):
        t1.destroy()
        t2.destroy()
        t3.destroy()
        bigFrame2 = Frame(root)
        bigFrame2.pack(ipadx= 100)
        MainSearch(bigFrame2)
class MainSearch():

    def func(self):
        self.get_data2()

    def __init__(self, master):
        testFrame = Frame(master)
        test = Label(testFrame)
        test.pack()

        self.style = Style()
        self.master = master

        settingsFrame = Frame(master)
        settingsFrame.pack(fill = X, side = TOP)

        searchFrame = Frame(master)
        searchFrame.pack(side = TOP)

        bottomFrame = Frame(master)
        bottomFrame.pack(side = TOP)

        self.settingsButton = Button(settingsFrame,  image = photo, width = 30, command = lambda : rofl(master))
        self.settingsButton.pack(side = LEFT, padx = 5, pady = 5)

        self.Title = Label(searchFrame, text="Enter the team you want to look up below:")
        self.Title.pack()

        self.searchBar = Entry(searchFrame)
        self.searchBar.pack(pady = 2)

        self.button = Button(searchFrame, text="Search", command=self.get_data2)
        self.button.pack()

        self.resultTitle = Label(bottomFrame, text = "Results:")
        self.resultTitle.pack(pady = 5)

        self.StatList = Listbox(bottomFrame, width=40)
        self.StatList.pack(ipadx=5)

        self.master.bind('<Return>', self.get_data)

    def get_data(self, event):
        global entryText
        global result
        global rank
        if self.searchBar.get().upper().strip() in teams:

            self.StatList.delete(0, END)
            self.StatList.insert(END, "Most recent tournament rank: " + str(database[teams.index(self.searchBar.get().upper().strip())]['rank']))
            self.StatList.insert(END, "Win Points:  " + str(database[teams.index(self.searchBar.get().upper().strip())]['wp']))
            self.StatList.insert(END, "Auton Points: " + str(database[teams.index(self.searchBar.get().upper().strip())]['ap']))
            print(database[teams.index(self.searchBar.get().upper().strip())])
            result = 1
        if result == 0:
            self.StatList.delete(0,END)
            self.StatList.insert(END, "No results.")

    def get_data2(self):
        global entryText
        global result
        global rank
        if self.searchBar.get().upper().strip() in teams:

            self.StatList.delete(0, END)
            self.StatList.insert(END, "Most recent tournament rank: " + str(database[teams.index(self.searchBar.get().upper().strip())]['rank']))
            self.StatList.insert(END, "Win Points:  " + str(database[teams.index(self.searchBar.get().upper().strip())]['wp']))
            self.StatList.insert(END, "Auton Points: " + str(database[teams.index(self.searchBar.get().upper().strip())]['ap']))
            print(database[teams.index(self.searchBar.get().upper().strip())])
            result = 1
        if result == 0:
            self.StatList.delete(0,END)
            self.StatList.insert(END, "No results.")

result = 0
rank = StringVar()
wp = StringVar()
ap = StringVar()
testList = ["a", "b"]

entryText = StringVar()


b = MainSearch(bigFrame)
root.mainloop()