# Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
i=1
s=0
while i<=10:
    s=s+(1/i)
    i=i+1
print(s)

