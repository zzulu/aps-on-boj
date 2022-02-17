def get_pi(P):
    l = len(P)
    pi = [0] * l
    begin = 0
    for index in range(1, l):
        while (begin > 0 and P[index] != P[begin]):
            begin = pi[begin-1]
        
        if (P[index] == P[begin]):
            begin += 1
            pi[index] = begin
    return pi


text = input()
L = len(text)

max_value = 0
for i in range(L):
    new_value = max(get_pi(text[i:]))
    if max_value < new_value:
        max_value = new_value

print(max_value)
