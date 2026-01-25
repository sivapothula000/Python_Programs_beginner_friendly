import turtle
import random
turtle.bgcolor("black")
tur=turtle.Turtle()
width=5
length=7
dot_distance=25
tur.speed(0)
tur.setpos(-250,250)
tur.color("red")
tur.penup()
colors=["red",
"blue",
"green",
"yellow",
"purple",
"orange",
"white",
"cyan",
"magenta"
]
def spiral(m,n):
    
    k=0
    l=0
    f=0
    #k=index of starting row
    #l=index of starting column
    col=random.randint(0,8)
    tur.color(colors[col])
    while(k<m and l<n):
        if f==1:
            tur.right(90)
        #printing the first row 
        for i in range(l,n):
            tur.dot()
            tur.forward(dot_distance)
            #print(a[k][i],end=" ")
        k+=1
        f=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(colors[col])
        #printing the last column
        for i in range(k,m):
            tur.dot()
            tur.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        n-=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(colors[col])
        if(k<m):
            #printing  the last row values
            for i in range(n-1,l-1,-1):
                tur.dot()
                tur.forward(dot_distance)
               # print(a[m-1][i],end=" ")
            m-=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(colors[col])
        if(l<n):
            #printing the first coulmn
            for i in range(m-1,k-1,-1):
                tur.dot()
                tur.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1

'''a=[]
count=1
o=int(input("Enter the array size:"))

for i in range(o):
    l=[]
    for j in range(o):
        l.append(count)
        count+=1
    a.append(l)'''
#p=int(input("Enter the array size:"))
spiral(20,20)
turtle.done()

