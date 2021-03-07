A, B, V = map(int, input().split())
print(((V-B)//(A-B))+1) if (V-B)%(A-B) else print(((V-B)//(A-B)))
