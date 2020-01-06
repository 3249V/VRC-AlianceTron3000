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
    #frame2.destroy()
    #gamer()
    print(len(teams))
    root.destroy()
    #c=Loading(self.master)
    print('test')
  def done2(self):
    self.dataFunc()
    #frame2.destroy()
    #gamer()
    print(len(teams))
    root.destroy()
    #c=Loading(self.master)
    print('test')
  def get_data1(self, sku):

    tempTeams = vexdb.getTeams(sku=sku)
    #print(tempTeams)
    for i in range(len(tempTeams)):
      teams.append(tempTeams[i]['number'])
    print(teams)
    compData.set(vexdb.getEvents(sku = sku)[0]['name'])
    compLocation.set(str(vexdb.getEvents(sku = sku)[0]['loc_city'])+ ", " + vexdb.getEvents(sku = sku)[0]['loc_region'])


  def __init__(self, master):
    #compData = StringVar()
    self.master = master
    #self.frame1 = Frame(root)
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
"""

"""
def gamer():
  c = Loading(root)

#gamer()
a = DefData(root)
#d = Loading(root)

listOfTeams = ["866A",
               "866B",
               "866C",
               "866D",
               "866E",
               "866F",
               "866G",
               "1460E",
               "1460K",
               "1460M",
               "1460S",
               "1460W",
               "1812A",
               "1812B",
               "1812C",
               "1812D",
               "1812X",
               "1812Z",
               "2990B",
               "2990C",
               "2990G",
               "3249C",
               "3249G",
               "3249H",
               "3249R",
               "3249S",
               "3249U",
               "3249V",
               "5686B",
               "5686C",
               "5686D",
               "5686E",
               "5686F",
               "5686G",
               "5686H",
               "9391A",
               "9391B",
               "9391C",
               "9391D",
               "11761B",
               "11761F",
               "11761X",
               "18379A",
               "18379B",
               "18379C",
               "22300A",
               "22300B",
               "51581A",
               "51581B",
               "51581C",
               "51581D",
               "65194D",
               "65194M",
               "65194T",
               "73268R",
               "85904A",
               "85904B",
               "85904C",
               "97381A",
               "98558A",
               "98558B",
               "98558R"]

# print (len(listOfTeams))





mainloop()

#teams = [("3249V", 3, 10), ("3249C", 16, 4)]
