import random

class conway:
   def __init__(self, numLists,numInts,genMethod):
      self.store = []
      self.numLists = numLists
      self.numInts = numInts
      self.genMethod = genMethod

      for i in range (0, numLists,1):
         temp = []

         for j in range(0,numInts,1):
            if genMethod == "zeros":
               temp = temp + [0]
            else:
               temp = temp +[random.randint(0,1)]

         self.store = self.store + [temp]

   def getDisp(self):
      accum = ""

      for i in range (0,self.numLists,1):
         for j in range (0,self.numInts,1):
            if self.store[i][j] == 0:
               accum = accum + " "
            else:
               accum = accum + "*"

         accum = accum + "\n"

      return accum

   def printDisp(self):
      string = self.getDisp()
      print(string)
      return True

   def setPos(self,row,col,val):
      if val != 0 and val != 1:
         return False
      else:
         self.store[row][col] = val
         return True

   def getNeighbours(self,row,col):
      left = 0
      right = 0
      up = 0
      down = 0
      rows = []
      cols = []
      accum = []
      
      if col == 0:
         left = len(self.store[row])-1
         right = 1
      elif col == len(self.store[row])-1:
         left = col - 1
         right = 0
      else:
         left = col - 1
         right = col + 1
      cols = [left,col,right]

      if row == 0:
         up = len(self.store)-1
         down = 1
      elif row == len(self.store)-1:
         up = row - 1
         down = 0
      else:
         up = row - 1
         down = row + 1
      rows = [up,row,down]

      counter = 0
      for i in range(0,3,1):
         for j in range(0,3,1):
            if counter != 4:
               accum = accum + [self.store[rows[i]][cols[j]]]
            counter = counter + 1
      
      return accum
