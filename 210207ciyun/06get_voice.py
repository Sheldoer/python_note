"""
@File    ：插入音频.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import moviepy.editor as mpy

# 读取词云视频
my_clip = mpy.VideoFileClip('result.mp4')
# 截取背景音乐
audio_background = mpy.AudioFileClip('song.mp4').subclip(17, 42)
audio_background.write_audiofile('vmt.mp3')
# 视频中插入音频
final_clip = my_clip.set_audio(audio_background)
# 保存为最终的视频   动听的音乐！漂亮小姐姐词云跳舞视频！
final_clip.write_videofile('final_video.mp4')
