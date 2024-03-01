x= open("demofile.txt",r)
print(x.read())

y=open("demofile.txt",a)
y.write("hello")
y.close()
y=open("demofile.txt")
print(y.read())

z=open("demofile.txt",w)
z.write("overwright")
z.close()
open("demofile.txt", "r")
print(z.read())

x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist




x.read()
x.write("hi")
x.close()
