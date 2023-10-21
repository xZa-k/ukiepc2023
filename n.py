from decimal import Decimal
from math import ceil


wine_count = int(input())

wine_sizes = []
for i in range(wine_count):
    raw = input()[:-1]
    # print(raw)
    size = Decimal(raw)
    size = size * 10**10
    wine_sizes.append(str(int(size)))
    
# print(wine_sizes)

for wine in wine_sizes:
    for n in wine:
        print(chr(int(n) + 97), end="")
    print()
