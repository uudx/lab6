from time import sleep
from math import sqrt

num = int(input())
time = float(input())
sleep(time/100)
sqrt = sqrt(num)
print(f"Square root of {num} after {time} miliseconds is {sqrt}")
