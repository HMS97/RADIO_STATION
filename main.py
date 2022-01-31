from path import Path
from musicdl import musicdl
from pydub import AudioSegment
import random
# config = {'logfilepath': 'musicdl.log', 'savedir': 'Downloads/songs/', 'search_size_per_source': 5, 'proxies': {}}
# target_srcs = ['migu']
# client = musicdl.musicdl(config=config)
# search_results = client.search('说好不哭', target_srcs)
# for key, value in search_results.items():
#     client.download(value[0:1])
#     break
stop = False
new_song = AudioSegment.from_file("Sound recordings/begin.m4a")
middle = AudioSegment.from_file("Sound recordings/midle.m4a")
end = AudioSegment.from_file("Sound recordings/end.m4a")
while(1):
    for item in Path('Downloads/songs/').files():
        song = AudioSegment.from_file(item)
        new_song = new_song + song
        if (new_song.duration_seconds/60) < 110:
            if  0 < abs(20 - (new_song.duration_seconds/60)%20) < 5:
                new_song += middle
            if  0 < abs(40 - (new_song.duration_seconds/60)%40) < 5:
                for item in random.choices([i for i in Path('Sound recordings/').files() if len(i.name)> 10],k = 2):
                    adv = AudioSegment.from_file(item)
                    new_song += adv
        if new_song.duration_seconds/60 > 115:
            stop = True
            new_song += end
            break
    if stop == True:
        song = AudioSegment.from_file(random.choice(Path('Downloads/songs/').files()))
        new_song += song
        end_seconds = 60 * 1000* 117
        new_song = new_song[:end_seconds]
        break
new_song.export("songs_radiao.mp3", format="mp3")
