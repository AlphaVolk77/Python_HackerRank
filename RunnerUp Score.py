n = int(input())
arr = list(map(int, input().split()))
a = max(arr)
x = arr.count(a)
arr.sort(reverse=True)
print(arr[x])