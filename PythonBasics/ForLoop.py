obj = [2, 3, 4, 5]
for i in obj:
    print(i)
# to print the multiple of 2
    print(i*2)

print('&&&&&&& sum of natural numbers &&&&')
# to print the sum of first five natural numbers
# range(i, j) > i to j-1
sum1 = 0
for i in range(1, 6):
    sum1 = sum1 + i
print(sum1)

print('*********to skip the iteration count*********')
# to print the numbers with a gap of +2, it will be like i=1: i<10; i+2
# here third no defines the gap between the numbers to print
for i in range(1, 10, 2):
    print(i)

print('########## skip the first index #########')
# if you skip the first index then the range will start from 0
# it has only upper bound
for i in range(4):
    print(i)
