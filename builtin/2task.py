string = input()

countup = 0
countlo = 0

for i in string:
    if i.isupper():
        countup+=1
    elif i.islower():
        countlo+=1

print(f"upper casr letters: {countup}, lower case letters: {countlo}")
