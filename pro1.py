# File Handling

file = open("test.txt", "r")
# Reading File Line By Line
for line in file:
    print(line)
file.close()

# Read By Characters
file = open("test.txt", "r")
n = 1
chunk = file.read(n)
while chunk != '':
    print(chunk)
    chunk = file.read(n)
file.close()

# Seek Read
file = open("test.txt", "r+")
file.read(10)
print("Current :", file.tell())
file.seek(0, 0)
print(file.read(10))
file.close()
