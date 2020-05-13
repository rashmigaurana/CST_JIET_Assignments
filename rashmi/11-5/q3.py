t=int(input("enter number of test case: "))
for i in range(0,t):
    n=int(input("enter number of blocks: "))
    stair=0
    i=1
    while n>0:
        n=n-i
        i=i+1
        if n>=0:
            stair+=1
    print(stair)
