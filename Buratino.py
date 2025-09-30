import sys

N, L, T, M = map(int, sys.stdin.readline().split())

cycles = M // T
result = cycles * N * L

print(result)