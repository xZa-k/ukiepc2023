import itertools
from math import ceil, floor


song_amount, refresh_time = map(int, input().split(" "))
songs = list(map(int, input().split(" ")))


# ranked_songs = sorted(songs, True)
# for i in range(len(ranked_songs)):

for i in range(len(songs)):
    if songs[i] > refresh_time:
        songs[i] = refresh_time
    
# print(songs)
# ads = [0 for i in range(song_amount)]
for start in range(song_amount):
    time = 0
    ads = 0
    
    end = (start + song_amount-1) % (song_amount)

    # ads
    # print(end)
    
    ads = ceil(((sum(songs) - (songs[end])) / refresh_time)) - 1
    
    # for n in range(song_amount):
    #     i = (start + n) % song_amount
    #     time += songs[i]

    #     if n != song_amount - 1 and time >= refresh_time:
    #         time = 0
    #         ads += 1
    if ads < 0:
        ads = 0
    print(ads, end=" ")
    # print(ads)