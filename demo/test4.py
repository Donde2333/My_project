# -*- coding: UTF-8 -*-

song_num = int(input("你想记录几首歌？："))
songs = {}

for x in range(song_num):
    song_name = input("输入歌名：")
    song_arts = input("输入作者：")
    songs.update({song_name:song_arts})

def write_like_songs(songs,filename):
    with open(filename,"w") as f:
        f.write("喜爱的歌单：\n")
        for key,value in songs.items():
            f.write(f"{key} by {value}\n")

write_like_songs(songs,"like_songs.txt")
print(songs)
