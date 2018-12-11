# Exception Handling While File Handling

try:
    file = open("tst.txt","r")
    print(file.read())
except Exception as e:
    print("Error Reading/Opening File: ",str(e))

