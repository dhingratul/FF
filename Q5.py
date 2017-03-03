def apply_operation(left_operand,right_operand,argument):
  switcher = {
      '+': str(left_operand+right_operand),
      '-': str(left_operand-right_operand),
      '*': str(left_operand*right_operand),
      '/': str(left_operand/right_operand),
  }
  return switcher.get(argument, "nothing")

#Main Program  
print apply_operation(4,5,'*')
