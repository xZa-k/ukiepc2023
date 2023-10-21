import math

h1,d1,t1 =list(map(int, input().split(" ")))
h2,d2,t2 =list(map(int, input().split(" ")))
player1 = (math.ceil(h2 / d1) * t1) - t1
player2 = (math.ceil(h1 / d2) * t2) - t2

if abs(player1 - player2) <= 0.5:
    print("draw")
elif player1 > player2:
    print("player two")
else:
    print("player one")