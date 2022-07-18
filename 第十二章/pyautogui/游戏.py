# coding=gbk
"""
作者：川川
@时间  : 2022/3/19 19:29
"""
from pygame import mixer
from gtts import gTTS


def main():
    tts = gTTS('Learn Python from Medium')
    tts.save('python.mp3')
    mixer.init()
    mixer.music.load('python.mp3')
    mixer.music.play()


if __name__ == "__main__":
    main()
