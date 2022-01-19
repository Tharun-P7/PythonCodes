a = [-2, -3, 4, -1, -2, 1, 5, -3]
max_so_far=-100000
max_ending=0
start=0
end=0
s=0
for i in range(0,len(a)):
    max_ending+=a[i]
    if(max_so_far<max_ending):
        max_so_far=max_ending
        start=s
        end=i
    if(max_ending<0):
        max_ending=0
        s+=1
print(max_so_far,start,end)
