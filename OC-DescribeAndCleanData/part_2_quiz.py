import pandas as pd

list = [1,10,1,10,1,1,5,1,5,5] 
   
# create series form a list 
ser = pd.Series(list) 
print("Mean ="+str(ser.mean())) 
print("Med ="+str(ser.median()))
print("Mode ="+str(ser.mode()))


list_a = [6,4,6,4,6,4,6,4]
list_b = [1,4,1,4,1,4,1,4]
ser_a = pd.Series(list_a)
ser_b = pd.Series(list_b) 
print("Var A ="+str(ser_a.var(ddof=0))) 
print("Var B ="+str(ser_b.var(ddof=0)))

input()
