f=open("catch.txt",'r+')
f.seek(0)
d=f.write('Hello world')
print(d)