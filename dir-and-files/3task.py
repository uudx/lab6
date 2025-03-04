import os
path = 'D:\\projects\\'
if os.path.exists(path):
    print("Files: ")
    for i in os.listdir(path):
        print(i)
    print("\nDirectory in portion: ")
    for i in path.split("\\"):
        print(i)
