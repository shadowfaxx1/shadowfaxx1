
# cook your dish here
t=int(input())
for i in range(t):
    l3=[]
    n,k=map(int,input().split())
    l1=list((input().split()[:n]))
    for i in range(k):
        l2=list((input().split()))
    s1=set(l1)
    s2=set(l2)
    d=s1.intersection(s2)
    l3=list(d)
    for i,j in zip(l1,l3):
        if(i==j):
            print("yes")
        else:
            print("no")
    
    
    
    
                
                

    
    
    