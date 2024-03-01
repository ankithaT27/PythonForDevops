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
