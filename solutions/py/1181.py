N = int(input())
words = list({input() for _ in range(N)})
words.sort(key=lambda word: (len(word), word))
for word in words:
    print(word)
