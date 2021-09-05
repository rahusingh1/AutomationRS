# # # with open('demo.txt') as countletter:
# # #     count = 0
# # #     text = countletter.read()
# # #     for character in text:
# # #         if character.isupper():
# # #             count += 1
# # # print(count)
# # #
# # # func = lambda x:return(x*x)
# # # print(func(2))
# #
# # # Program to add two matrices using nested loop
# #
# # X = [[12, 7, 3],
# #      [4, 5, 6],
# #      [7, 8, 9]]
# #
# # Y = [[5, 8, 1],
# #      [6, 7, 3],
# #      [4, 5, 9]]
# #
# # result = [[0, 0, 0],
# #           [0, 0, 0],
# #           [0, 0, 0]]
# #
# # # iterate through rows
# # for i in range(len(X)):
# #     # iterate through columns
# #     for j in range(len(X[0])):
# #         result[i][j] = X[i][j] + Y[i][j]
# #
# # for r in result:
# #     print(r)
#
# # rows = int(input("Enter the number of rows: "))
# #
# # # Outer loop will print the number of rows
# # for i in range(0, rows):
# #     # This inner loop will print the stars
# #     for j in range(0, i + 1):
# #         print("*", end=' ')
# #         # Change line after each iteration
# #     print(" ")
# # # For second pattern
# # for i in range(rows + 1, 0, -1):
# #     for j in range(0, i - 1):
# #         print("*", end=' ')
# #     print(" ")
#
# # r = int(input().strip())
# r = 3
#
# for i in range(0, r):
#     for j in range(0, i+1):
#         print("*", end=' ')
#     print("")
# for i in range(r+1, 0, -1):
#     for j in range(0, i-1):
#         print("*", end=' ')
#     print("").

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = int(input())
for i in range(s):
    for j in range(s):
        if(i==0 or i == s-1 or j==0 or j == s-1):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()