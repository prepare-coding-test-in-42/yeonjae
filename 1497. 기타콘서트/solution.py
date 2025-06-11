from itertools import combinations

def solution():
    N, M = map(int, input().split())
    guitars = [list(input().split()) for _ in range(N)]

    for guitar in guitars:
        songs = []
        for idx in range(len(guitar[1])):
            if guitar[1][idx] == "Y":
                songs.append(idx)
        guitar[1] = songs

    max_song_cnt = 0
    min_guitar_cnt = 10

    for num in range(1, N + 1):
        combs = combinations(guitars, num)
        for comb in combs:
            total = set()
            for guitar in comb:
                total.update(guitar[1])
            song_count = len(total)
            if song_count > max_song_cnt:
                max_song_cnt = song_count
                min_guitar_cnt = num
            elif song_count == max_song_cnt:
                min_guitar_cnt = min(min_guitar_cnt, num)
    
    if max_song_cnt == 0:
        return -1
    else:
        return min_guitar_cnt

if __name__ == "__main__":
    print(solution())