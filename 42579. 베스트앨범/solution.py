class genre:
    def __init__(self, total, first_index, second_index, first_plays, second_plays):
        self.total = total
        self.first_index = first_index
        self.second_index = second_index
        self.first_plays = first_plays
        self.second_plays = second_plays

def solution(genres, plays):
    length = len(genres)

    album = {}
    for index in range(length):
        name = genres[index]
        if name not in album:
            album[name] = genre(plays[index], index, -1, plays[index], -1)
        else:
            album[name].total += plays[index]
            if plays[index] > album[name].first_plays:
                album[name].second_index = album[name].first_index
                album[name].second_plays = album[name].first_plays
                album[name].first_index = index
                album[name].first_plays = plays[index]
            elif plays[index] > album[name].second_plays:
                album[name].second_index = index
                album[name].second_plays = plays[index]

    sorted_album = sorted(album.items(), key=lambda x : x[1].total, reverse=True)
    
    result = []
    for item in sorted_album:
        result.append(item[1].first_index)
        if item[1].second_index != -1:
            result.append(item[1].second_index)

    return result