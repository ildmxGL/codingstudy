def solution(genres, plays):
    answer= []
    dict_genres_count = dict()
    dict_genres_index = dict()
    
    for idx, genre in enumerate(genres):
        if genre in dict_genres_count.keys():
            dict_genres_count[genre] += plays[idx]
            dict_genres_index[genre].append(idx)
        else:
            dict_genres_count[genre] = plays[idx]
            dict_genres_index[genre] = [idx]
    genre_list = [x for x, _ in sorted(dict_genres_count.items(), key=lambda x: x[1], reverse=True)]

    for genre in genre_list:
        songs_idx = dict_genres_index[genre]
        songs_play = [x for i, x in enumerate(plays) if i in songs_idx]
        songs_sort = [idx for idx, _ in sorted(zip(songs_idx, songs_play), key=lambda x: x[1], reverse=True)]
        answer += songs_sort[:2]

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
