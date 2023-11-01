import sys

n = int(input())
num_list = list(map(int, input().split()))
m = max(num_list)

for index in range(n):
    num_list[index] = num_list[index] / m * 100

print(sum(num_list) / n)