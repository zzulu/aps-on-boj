N = int(input())
cards = {}
for card in input().split():
    if cards.get(card):
        cards[card] += 1
    else:
        cards[card] = 1
M = int(input())
print(' '.join([str(cards.get(card, 0)) for card in input().split()]))
