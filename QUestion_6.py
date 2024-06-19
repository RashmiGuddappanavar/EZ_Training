'''Write a program sorts the array, finds the two largest elements, compute their average, and sets elements greater than or equal to this average to 0, then print the modified array.'''


n=int(input())
arr=list(map(int,input().split()))
arr.sort()
element1=arr[-1]
element2=arr[-2]
avg=(element1+element2)/2
sum=0
for i in range(len(arr)):
    if(arr[i]>=avg):
        arr[i]=0
    else:
        continue
print()  
