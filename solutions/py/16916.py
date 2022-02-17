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


def kmp(S, P):
    pi = get_pi(P)
    index, begin = 0, 0
    while index < len(S):
        while begin and S[index] != P[begin]:
            begin = pi[begin-1]
        if S[index] == P[begin]:
            if begin == len(P)-1:
                return 1
            else:
                begin += 1
        index += 1
    return 0


print(kmp(input(), input()))
