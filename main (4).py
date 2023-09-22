def fact (X):
  if  X ==1:
    return 1
  else:
    return (X*fact (X-1))
num = int(input("Enter the num :"))
print("the factorial is :",fact (num))