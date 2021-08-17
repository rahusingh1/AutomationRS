# Finally keyword in exception handling.
# you can use finally only if you use try and except mechanism.
# Code under finally will always run no matter, code in 'try' is pass or fail.
# purpose of finally keyword executing everytime:
# it is just like the tear down of the records created during running the code/scripts.
# suppose you created some records during testing
# sometimes test cases pass sometimes fails but the records are created everytime
# so to remove that records and clear the cookies and other resources
# you can use finally at the end of the code to free the resourse and cleanup the memory.
try:
    with open("/home/rahul/PycharmProjects/AutomationRS/PythonBasics/new.txt", "r") as reader:
        r = reader.read()
        print(r)
except:
    print("you come to the except block because code in try block failed.")
finally:
    print("Finally block for cleaning up the resources.")