string = input()
b = ""

for i in reversed(string):
    b +=i
print("The string is polindrome" if b == string else "The string is not polindrome")
