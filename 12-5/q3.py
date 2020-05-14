a=[[0,0,1,0],
   [1,0,0,1],
   [1,1,1,0]]
count=0
for j in range(3):
    sum=0
    for i in range(2):
        sum+=a[i][j]
    if sum%2==1:
        count+=1

print("output",count)
