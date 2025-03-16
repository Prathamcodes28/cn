a=[1,2,3,4,5,6,7]
b=int(input("enter a number:"))
for i in a:
    if i==b:
     c=1
     break
    else:
     c=0
if c==1:
    print("item found in an array")
else:
    print("item is not in an array")




