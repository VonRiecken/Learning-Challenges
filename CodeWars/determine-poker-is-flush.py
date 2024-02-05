def is_flush(cards):
    suit = 0
    for card in range(len(cards) - 1):
        if cards[card][-1] == cards[0][-1]:
            suit += 1

    if suit == 4:
        return True
    else:
        return False
