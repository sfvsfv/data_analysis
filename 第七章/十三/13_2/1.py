# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/8 20:24
"""
from moviepy.editor import *
clip = (VideoFileClip("bi.mp4"))
clip.write_gif("1.gif")
