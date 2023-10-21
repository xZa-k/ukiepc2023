noOfXYZ = list(map(int, input().split())) #0 = No of Piers, 1 = No of Cards, 2 = No of Events
events = []
for i in range(noOfXYZ[2]):
    events.append(list(map(int, input().split())))

cards = []
cardCosts = []

for i in range(noOfXYZ[1]):
    cards.append(-1)
    cardCosts.append(0)

for i in range(noOfXYZ[2]):
    curE = events[i]
    if cards[curE[1]-1] == -1:
        cards[curE[1]-1] = curE[0]
    else:
        cost = 0
        if curE[0] == cards[curE[1]-1]:
            cost = 100
        else:
            cost = abs(curE[0] - cards[curE[1]-1])
        cardCosts[curE[1]-1] += cost
        cards[curE[1]-1] = -1

for i in range(len(cards)):
    if cards[i] != -1:
        cardCosts[i] += 100
    # print(cardCosts[i], end=" ")
print(" ".join(map(str, cardCosts)))