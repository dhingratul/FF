def convert(input_string):
  # First character is a number betwen 0(ASCII=48) and 9(ASCII=57) 
  if  ord(input_string[0])>=48 and ord(input_string[0])<=57:
    if(len(input_string.split('.'))==1):
        #No float detected
      return int(input_string)
    else:
      return float(input_string)
  else:
    #If not a number, it is a character
    return input_string

#Main Program
print convert("ABC")
print convert("512")
print convert("25.25")