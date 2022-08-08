num=int(input("enter the number"))
tem=num
sum=0
order=len(str(num))
while tem>0:
    digit=tem%10
    sum=sum+(digit**order)
    tem=tem//10
if num==sum:
    print("am")
else:
    print("not")
