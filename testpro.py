from sys import argv 

script,file1,file2=argv

print("opening and displaying files ")
x=open(file2).read()
y=open(file1).read()

print(x,y)

z=open('test67.txt','w')
print(z.name)