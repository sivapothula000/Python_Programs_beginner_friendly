def bubble_sort(a):
    n=len(a)
    count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                count+=1
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
        print(count)
a=[5,4,3,2,1]

bubble_sort(a)
h=[]

for i in a:
    h.append(i)
print(h)
print(sorted(a)) #This is the direct function for sorting the elements in a list
a.sort()
print(a) #this is another method
      