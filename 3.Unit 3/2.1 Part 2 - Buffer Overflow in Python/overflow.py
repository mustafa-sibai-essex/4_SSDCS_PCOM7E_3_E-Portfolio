"""This program shows buffer overflow in python"""

buffer = [None] * 10

for i in range(0, 11):

    buffer[i] = 7

print(buffer)
