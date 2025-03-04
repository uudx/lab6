path = 'D:\\projects\\data.txt'
file = open(path, "w")

lst = ["some", "data", "leader","python"]

for i in lst:
    file.writelines(f"{i}\n")
file.close()

file = open(path, "r")
for i in file:
    print(i)
