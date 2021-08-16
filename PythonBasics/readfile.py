#Method to open the file in python is open()
file = open("/home/rahul/PycharmProjects/AutomationRS/PythonBasics/new.txt")
#method to read the file is read()
# read() will read all the contents of the file.
#print(file.read())

# read() method can read one bit at a time
# enter no of bits to read at a time as read(5)
#print(file.read(6))

# to read the data line wise use method readLine()
# it will read one single line at a time
#print(file.readline())
#print(file.readline())

# print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#to read all lines of the file same as read method
#but each line will get stored in a list, at 0th index first line will be stored, at 1st index second line.
# if it is in list then you can perform multiple operations like iteration using loops etc.
#print(file.readlines())
for line in file.readlines():
    print(line)

#it is good practice to close the file after reading it.
# to avoid memory leak or corrupt the file.
file.close()