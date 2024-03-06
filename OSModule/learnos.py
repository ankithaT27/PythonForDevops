#prints pwd
print("The present dir is", os.getcwd())
a=os.getcwd()
print(a)

#change dir
os.chdir("/workspaces")

#check if we are in a aprticular dir
if a=="/workspaces":
    print("yes you are")
else:
    print("no")

#change to a dir 
if a=="/workspaces":
    print("yes, right")
else:
    os.chdir("/workspaces")
    print("now we are in workspaces")
    print(os.getcwd())


os.mkdir("/workspaces/PythonForDevops/hello")


#checkif directory exists (bool is optional)
import os
a=bool(os.path.exists("/ankitha"))
print(a)

#check if a file exists
a=bool(os.path.isfile("/workspaces/PythonForDevops/OSModule/learnoss.py"))

#remove a dir
os.rmdir()
