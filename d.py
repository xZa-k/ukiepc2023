
no_couriers = int(input())
strengths = list(map(int, input().split(" ")))

sorted_strengths = sorted(strengths)

result = 0

teams = no_couriers // 3

biggest_idx = 1
minimum_idx = 0

for t in range(teams):
    biggest = sorted_strengths[-biggest_idx]
    biggest_idx += 1

    minimum = sorted_strengths[minimum_idx]
    minimum_idx += 1

    biggest = sorted_strengths[-biggest_idx]
    biggest_idx += 1

    result += biggest

print(result)