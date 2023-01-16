def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
arr = [2,5,8,9,10,16,22]
target = 22
print(linearSearch(arr, target))