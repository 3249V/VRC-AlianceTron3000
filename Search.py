from tkinter import *
import time
from tkinter.ttk import *
from LoadingTest import *

root = Tk()
photo = PhotoImage(file=r"C:\Users\Connor\Downloads\settings.png")
bigFrame = Frame(root)
bigFrame.pack(ipadx=100)
bigFrame2 = Frame(root)
AutonCheck = IntVar()
RankCheck = IntVar()
WPCheck = IntVar()
modeVar = IntVar()
searchsave = StringVar()
WPCheck.set(1)
RankCheck.set(1)
AutonCheck.set(1)


def rofl(frame2):
    bigFrame.destroy()
    frame2.destroy()
    what = Label(root, text="Not Finished Yet")
    what.pack(pady=10)

    RankCheckbox = Checkbutton(root, text="Show last tournament rank", variable=RankCheck)
    RankCheckbox.pack(pady=2)


    WPCheckbox = Checkbutton(root, text="Show Win Points", variable=WPCheck)
    WPCheckbox.pack(pady=2)


    checkbox = Checkbutton(root, text="Show Auton Points", variable=AutonCheck)
    checkbox.pack(padx=10, pady=2)

    if AutonCheck == 1:
        checkbox.select()
    idk = Button(root, text="Back", command=lambda: WhyEven(idk, what, checkbox, RankCheckbox, WPCheckbox))
    idk.pack(pady=10)



class WhyEven():
    def __init__(self, t1, t2, t3, t4, t5):
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()
        t5.destroy()
        bigFrame2 = Frame(root)
        bigFrame2.pack(ipadx=100)
        print("back")
        MainSearch(bigFrame2)


def mode_switch():
    #searchsave = self.searchBar.get()
    print(entryText)


class MainSearch():
    def __init__(self, master):
        testFrame = Frame(master)
        test = Label(testFrame)
        test.pack()

        self.style = Style()
        self.master = master

        settingsFrame = Frame(master)
        settingsFrame.pack(fill=X, side=TOP)
        searchFrame = Frame(master)
        searchFrame.pack(side=TOP)

        bottomFrame = Frame(master)
        bottomFrame.pack(side=TOP)

        self.settingsButton = Button(settingsFrame, image=photo, width=30, command=lambda: rofl(master))
        self.settingsButton.pack(side=LEFT, padx=5, pady=5)

        self.Title = Label(searchFrame, text="Enter the team you want to look up below:", textvariable = entryText)
        self.Title.pack()

        self.searchBar = Entry(searchFrame, textvariable = entryText)
        print("Entry: "+ str(entryText))
        self.searchBar.pack(pady=2)

        self.button = Button(searchFrame, text="Search", command=self.get_data)
        self.button.pack()

        self.resultTitle = Label(bottomFrame, text="Results:")
        self.resultTitle.pack(pady=5)

        self.StatList = Listbox(bottomFrame, width=40)
        self.StatList.pack(ipadx=5)
        self.mode = Radiobutton(master, text="Search Team stats", variable=modeVar, value=1)
        self.mode.pack()
        self.mode = Radiobutton(master, text="Alliance Picker", variable=modeVar, value=2)
        self.mode.pack()

        self.master.bind('<Return>', self.get_data)

    def get_data(self, e=None):
        global entryText
        global result
        #global rank

        print(entryText)
        entryText = self.searchBar.get().upper().strip()
        if entryText in teams:

            print(entryText)
            self.StatList.delete(0, END)
            if RankCheck.get() == 1:
                self.StatList.insert(END, "Most recent tournament rank: " + str(
                    database[teams.index(entryText)]['rank']))
            if WPCheck.get() == 1:
                self.StatList.insert(END, "Win Points:  " + str(
                    database[teams.index(entryText)]['wp']))
            if AutonCheck.get() == 1:
                self.StatList.insert(END, "Auton Points: " + str(
                    database[teams.index(entryText)]['ap']))
            #print(AutonCheck)

            result = 1
        if result == 0:
            self.StatList.delete(0, END)
            self.StatList.insert(END, "No results.")

    def callback(self, *args):
    #if modeVar.get() == 2:
        #alliance_picker(Tk().settingsFrame)
        print("mode has changed")
        mode_switch()

    modeVar.trace("w", callback)

result = 0
rank = StringVar()
wp = StringVar()
ap = StringVar()
testList = ["a", "b"]

entryText = StringVar()

b = MainSearch(bigFrame)

root.mainloop()
