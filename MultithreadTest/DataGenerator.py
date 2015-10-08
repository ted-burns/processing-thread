__author__ = 'ltdwkst1'

with open("data.txt", 'w') as f:
    for i in range(1, 10000000, 1):
        f.write(str(i))