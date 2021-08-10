def CharOccur(str, x):
    count = 0
    ch = 0
    for i in str:
        if i == x:
            count += 1
    return count

str = "Rahul Singh"
x = "h"
print("{} occurs {} times in {}".format(x, CharOccur(str, x), str))