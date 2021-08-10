str = "geeksforgeeks"

freq = {}

for ele in str:
    if ele in freq:
        freq[ele] += 1
    else:
        freq[ele] = 1

print("Elements with frequency are: \n", freq)