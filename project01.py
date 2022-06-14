#creat a calculator for kirana store
sum=0
while(True):
    userinput=input("Enter the item price or press q to quit:\n")
    if(userinput!="q"):
        sum=sum + int(userinput)
        print(f"order total so far:{sum}")
    else:
        print(f"your bill total is {sum}.thannks for shopping with us")
        break