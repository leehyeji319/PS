# 음악 제목, 재생이 시작되고 끝난 시각, 악보
# C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환
# musicinfos - 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보

def music_note_replace(str):
    str = str.replace('C#', 'c')
    str = str.replace('D#', 'd')
    str = str.replace('F#', 'f')
    str = str.replace('G#', 'g')
    str = str.replace('A#', 'a')

    return str

def solution(m, musicinfos):
    m = music_note_replace(m)
    able_music = []
    for i, musicinfo in enumerate(musicinfos):
        
        start_time, end_time, music_name, music_note = musicinfo.split(",")
        music_note = music_note_replace(music_note)
        playing_time = abs((int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1])) - (int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1])))
        if len(music_note) <= playing_time:
            real_music_note = ""
            for j in range(playing_time // len(music_note)):
                real_music_note += music_note
            real_music_note += music_note[:playing_time % len(music_note)]
        else:
            real_music_note = music_note[:playing_time + 1]
        # print(real_music_note)
        if m in real_music_note:
            able_music.append([playing_time, i, music_name])

    able_music.sort(key=lambda x: (-x[0], x[1]))
    print(able_music)
    if len(able_music) == 0:
        return "(None)"
    else:
        return able_music[0][2]
    

print(solution("ABC",  ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))
