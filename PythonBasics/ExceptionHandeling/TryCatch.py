# if you think test case may fail and don't want to stop the testcases execution there,
# then you should use try and catch(in python- except):
# wrap the code that may fail in try block.
# if code is in try block it will raise exception if there is any and control will send to catch block.
# in catch block- you can write statement about the error, why you reached to this block.
# if you write code normally then it show error if code fails and testcase stops there.
try:
    with open("PythonBasics/new.txt", 'r') as reader:
        reader.read()

except:
    print("try block is failed so it reached to this block")

# To know the error thrown by python write the following code:
try:
    with open("PythonBasics/new.txt", 'r') as reader:
        reader.read()

except Exception as e:
    print(e)