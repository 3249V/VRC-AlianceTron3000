import vexdb
from tkinter import *
from tkinter.ttk import *

root = Tk()

database = []


compData = StringVar()
compLocation = StringVar()
teams = []

frame2 = Frame(root)

multNum = 1

class DefData():
  def dataFunc(self):
    self.get_data1(self.compSearch.get().upper().strip())
  def done(self, event):
    self.dataFunc()
    print(len(teams))
    root.destroy()
    print('test')
  def done2(self):
    self.dataFunc()
    print(len(teams))
    root.destroy()
  def get_data1(self, sku):

    tempTeams = vexdb.getTeams(sku=sku)
    #print(tempTeams)
    for i in range(len(tempTeams)):
      teams.append(tempTeams[i]['number'])
    print(teams)
    compData.set(vexdb.getEvents(sku = sku)[0]['name'])
    compLocation.set(str(vexdb.getEvents(sku = sku)[0]['loc_city'])+ ", " + vexdb.getEvents(sku = sku)[0]['loc_region'])


  def __init__(self, master):
    self.master = master
    title = Label(master, text = "Enter the SKU of the competition below: \n Note: All SKU's start with RE-VRC-19- with four identifying digits at the end", justify = CENTER)
    title.pack()

    self.compSearch = Entry(master)
    self.compSearch.pack(pady = 5)
    self.compSearch.insert(0, "RE-VRC-19-8321")
    self.compName = Label(master, textvariable=compData)
    self.compName.pack()

    #self.compLoc = Label(master, textvariable=compLocation)
    #self.compLoc.pack()
    self.enter = Button(master, text = "Confirm", command = self.done2)
    self.enter.pack()

    self.master.bind('<Return>', self.done)

def gamer():
  c = Loading(root)

a = DefData(root)
mainloop()
