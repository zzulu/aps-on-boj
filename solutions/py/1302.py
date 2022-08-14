N = int(input())

books = {}
for _ in range(N):
    book = input()
    if books.get(book):
        books[book] += 1
    else:
        books[book] = 1

print(min(books.items(), key=lambda book: (-book[1], book[0]))[0])
