import os
path = 'D:/projects'
#os.mkdir(path+"\\for_test")
a = "QWERTYUIOPASDFGHJKLZXCVBNM"
for i in a:
    with open(path+"/data.txt", "r") as src, open(path+f"/for_test/{i}.txt", "w") as dest:
        dest.write(src.read())
