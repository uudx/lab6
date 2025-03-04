path = 'D:\\projects\\data.txt'
file = open(path, "r")

count = 0
for i in file.read():
    if i.isdigit():
        count +=1
print(count)
