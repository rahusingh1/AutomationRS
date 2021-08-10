def reverse(arr, n):
    for i in range(n-1, -1, -1):
        print(arr[i])


if __name__ =='__main__':
    arr = [3, 5, 6, 8, 10]
    n = len(arr)
    print("array is: ", arr)
    reverse(arr, n)
