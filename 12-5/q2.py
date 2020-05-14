def linearsrch(mat,a,x):
    i=0
    j=a-1
    while(i<a and j>=0):
        if mat[i][j]==x:
            print("found at(",i,",",j,")")
            return 1
        if(mat[i][j]>x):
            j-=1
        else:
            i+=1
    print("not found")
    return 0

y=[ [10,20,30,40],
    [15,25,35,45],
    [27,29,37,48],
    [32,33,39,50] ]
b=int(input("enter the element to be searched: "))
linearsrch(y,4,b)
