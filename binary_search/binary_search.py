def binary_search(a,x):
    fos=0
    los=len(a)-1
    flag=0
    while(fos<=los and flag==0):
        mid=(fos+los)//2
        if (x==a[mid]):
            flag=1
            print("The element find at position:"+str(mid))
            return
        else:
            if(x<a[mid]):
                los=mid-1
            else:
                fos=mid+1
    print("The value is not found")
a=[1,2,3,4,5,6,7,8,9,10]
binary_search(a,5)
