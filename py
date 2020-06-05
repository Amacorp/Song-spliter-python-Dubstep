def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())
    
    
or


def song_decoder(song):
    song = song.split('WUB')
    newsong = []
    for i in song:
        if i != '':
            newsong += [i]
    return ' '.join(newsong)


or


import re

def song_decoder(song):
    return re.sub(r'(WUB)+', ' ', song).strip()
