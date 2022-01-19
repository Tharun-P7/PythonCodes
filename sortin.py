a=[7,5,6,2,10,3,5]
#BUBBLE SORT
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
#INSERTION SORT
a=[7,5,6,2,10,3,5]
for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while(temp<a[j] and j>=0):
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)
#SELECTION SORT
array=[7,5,6,2,10,3,5]
for i in range(len(a)):
    pos=i
    for j in range(i+1,len(a)):
        if(array[pos]>array[j]):
            pos=j
    if(pos!=i):
        temp=array[pos]
        array[pos]=array[i]
        array[i]=temp
print(array)
#MERGE SORT
def merge(a,i1,j1,i2,j2):
    k=0
    temp=[]
    while(i1<=j1 and i2<=j2):
        if(a[i1]<a[i2]):
            temp.append(a[i1])
            i1+=1
        else:
            temp.append(a[i2])
            i2+=1
    while(i1<=j1):
        temp.append(a[i1])
        i1+=1
    while(i2<=j2):
        temp.append(a[i2])
        i2+=1
    i=i1
    j=0
    while(i<=j2):
       a[i]=temp[j]
       i+=1
       j+=1
def mergesort(a,i,j):
    mid=(i+j)//2
    if(i<j):
        mergesort(a,i,mid)
        mergesort(a,mid+1,j)
        merge(a,i,mid,mid+1,j)
a=[7,5,6,2,10,3,5]
n=len(a)
mergesort(a,0,n-1)
print(a)
