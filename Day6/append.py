x=open("demofile121.txt","a")
x.write("Now the file has more content!")
x.close()

x=open("demofile121.txt","r")
print(x.read())
