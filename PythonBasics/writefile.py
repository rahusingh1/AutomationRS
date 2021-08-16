# To avoid writing the code for opening and closing files in 2 line, you can use following code.
# below is the optimized code to open and close the file.

# in this method if you open a file you need to tell to python in which mode you are opening this file either reading or writing.
# for reading mode give a flag 'r' for write use 'w'.
# with open('test.txt', 'r') as file:

# read the file and store all the lines in the list:
# reverse the list.
# write the reversed list back to the file.

with open("/home/rahul/PycharmProjects/AutomationRS/PythonBasics/new.txt", 'r') as reader:
    content = reader.readlines()
    print(content)
    reverse = reversed(content)
    with open("/home/rahul/PycharmProjects/AutomationRS/PythonBasics/new.txt", 'w') as writer:
        for line in reverse:
            writer.write(line)
    print("Code executed successfully")