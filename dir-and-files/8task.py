import os
path = 'D:/projects/for_test/'
a = "QWERTYUIOPASDFGHJKLZXCVBNM"
for i in a:
    g = os.path.exists(path+f"{i}.txt")
    print(g)
    if g:
        os.remove(path+f"{i}.txt")
        print(f"the file {i}.txt was removed")
    else:
        print("this file does not exist")
