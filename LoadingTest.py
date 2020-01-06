from tkinter import *

from Data import *
multNum = 100.0 / len(teams)
class Loading():
  def test(self, master):
      for i in teams:
          #print(len(teams))
          self.master = master
          self.progress['value'] = multNum * teams.index((i))
          self.master.update_idletasks()
          if len(vexdb.getRankings(team=i, season="current")) == 0:
              database.append(
                  {'wp': 0, 'team': i, 'wins': 0, 'ccwm': 0, 'ties': 0, 'trsp': 0, 'losses': 0, 'dpr': 0, 'sku': 0,
                   'division': 0, 'max_score': 0, 'opr': 0, 'ap': 0, 'sp': 0, 'rank': 0})
          else:
              database.append(vexdb.getRankings(team=i, season="current")[0])
          # print(vexdb.getRankings(team = i, season = "current")[0])
      print(database)
      root.destroy()
  def __init__(self, master):

    self.progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    self.progress.pack(pady=10)
    self.start = Button(root, text='Start', command= lambda : self.test(master)).pack(pady=10)
    multNum = 100.0 / len(teams)
root = Tk()
b = Loading(root)
root.mainloop()