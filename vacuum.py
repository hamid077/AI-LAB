def check(stack):
    if stack[-1]=="right" or stack[-1]=="left":
        if stack[-2]=="left" or stack[-2]=="right" :
            return False
stack=[]
flag=True
count=1
while flag:
    perc=input("enter the percept")
    loc=input("enter the location")
    if loc=="A":
        if perc=="dirty":
            print("action: suck...turn right")
            stack.append("suck")
            stack.append("right")  
        else:
            print("action: turn right")
            stack.append("right")
    else:
        if perc=="dirty":
            print("action: suck.....turn left")
            stack.append("suck")
            stack.append("left")
        else:
            print("action: turn left")
            stack.append("left")
    count=count+1
    if count>2:
        flag=check(stack)
print("both A and B are clean")
