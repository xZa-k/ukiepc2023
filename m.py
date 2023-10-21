square,stile,corner = list(map(int,input().split(" ")))
dist = 0
dist += square * 2

if stile > 0 and corner >= 2:
    dist += stile * 2 + 3
    corner -= 2


while corner > 1:
    dist += 3
    corner -= 2

print(dist) 
