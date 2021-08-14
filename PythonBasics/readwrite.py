#Method to open the file in python is open()
file = open("PythonBasics/new.txt")
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
#to read all lines of the file
#print(file.readlines())


#it is good practice to close the file after reading it.
# to avoide memory leak or corrupt the file.
file.close()