A, B, C = map(int, input().split())
center = (B if B > C else (C if A > C else A)) if A > B else (A if A > C else (C if B > C else B))
print(center)   

# print(sorted(list(map(int, input().split())))[1])
