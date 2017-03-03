class FindMin():
  def __init__(self,num1,num2,num3):
    self.num1=num1
    self.num2=num2
    self.num3=num3

  def find_min(self):
    smallest=self.num1
    if smallest > self.num2:
      smallest=self.num2
    if smallest > self.num3:
      smallest=self.num3
    return smallest  

# Main Program
x=FindMin(2,-1,25)
print x.find_min()
      