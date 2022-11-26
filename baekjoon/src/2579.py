import sys
input = sys.stdin.readline

# n=6
# arr=[10, 20, 15, 25, 10, 20]
n=int(input())
dp = [0 for _ in range(301)]
arr= [0 for _ in range(301)]    # n으로 주니까 indexError...
for i in range(n):
    # arr.append(int(input()))  #indexError...
    arr[i]=int(input())

# print(max(3, 5)) 이용할 것@@
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2]=max(arr[0]+arr[2], arr[1]+arr[2])
for i in range(3, n):
    dp[i]=max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[n-1])