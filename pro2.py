# Overwriting File
file = open("test.txt", "w+")
n = 1
while n <= 100:
    file.write("{0}\n".format(n))
    n += 1

file.close()


# Appending File
file = open("test.txt", "a+")
n = 1
while n <= 100:
    file.write("{0}\n".format(n))
    n += 1

file.close()