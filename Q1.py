from collections import Counter# For returnFrequency function

class newList:
  def __init__(self,items):
    self.mylist=items

  def getValue(self):
    return self.mylist
  
  def returnUnique(self):
    myset=set(self.mylist)
    return myset
  
  def returnFrequency(self):
    return Counter(self.mylist)
    
  def appendList(self,value):
    self.mylist.append(value)
    return self.mylist
    
  def insertList(self,key,value):
    self.mylist.insert(key,value)
    return self.mylist
    
# Main Program
L1=newList([1,2,3,4,1,4,"ABC","ABC"])
print L1.getValue()
print L1.returnUnique()
print L1.returnFrequency()
print L1.appendList(25)
print L1.insertList(2,12) # Insert 12 at index 2