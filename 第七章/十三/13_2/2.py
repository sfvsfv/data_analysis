# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/8 21:30
"""
from moviepy.editor import *
clip = (VideoFileClip("bi.mp4")
        .subclip(0, 3))
clip.write_gif("��ȡ.gif")
