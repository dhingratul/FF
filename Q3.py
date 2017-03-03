class PrintSentence:
  def __init__(self,value):
    self.value=value
  
  def __str__(self):
    strname=self.value[1]+" the "+self.value[0]+" is "+str(self.value[2])+" years old"
    return strname
    
# Main program
input_list=['dog','Fido',10]
NewObject=PrintSentence(input_list)
print NewObject
    
