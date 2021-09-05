def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1, 1):
        if i % 3 == 0 and i % 5 == 0:
            result = print("FizzBuzz")
            continue
        elif i % 3 ==0:
            result = print("Fizz")
            continue
        elif i % 5 == 0:
            result = print("Buzz")
            continue
        else:
            result = print(i)
            continue
        return result


if __name__ == '__main__':
    #n = int(input().strip())
    n = 15
    fizzBuzz(n)
