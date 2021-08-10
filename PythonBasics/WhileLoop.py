# while loop if the condition is true it will continuously executing the loop.
# it will continuously execute the loop until the condition becomes false.
s = 4

while s > 1:
    print(s)
    s = s - 1  # it is required to avoid the infinite loop
print("first while loop execution is done")

# if you don't want to print some no to be printed
t = 5
while t > 1:
    if t != 3:
        print(t)
    t = t - 1
print('second while loop execution is done')

# Break: it is used to break the entire while loop if certain condition is true
# it mostly used to check the certain element in the list.
u = 10
while u > 1:
    if u == 7:
        break
    print(u)
    u = u - 1
print('third while loop execution is done')

# Continue: it is used when you want to skip the current iteration and proceed to next iteration
# we can put multiple if condition in while loop
v = 10
while v > 1:
    if v == 9:
        v = v - 1   # it is used so that it will not go for infinite loop
                    # like if you find 9 it will stuck there because we are not decrease the value.
                    # it will skip the iteration of 9 and doen't print that.
        continue
    if v == 6:
        break
    print(v)
    v = v - 1
print('fourth while loop execution is done')