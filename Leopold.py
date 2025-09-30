import sys

N, L, K = map(int, sys.stdin.readline().split())

total = 0
weight = L
for _ in range(N):
    total += weight
    weight += K

print(total)