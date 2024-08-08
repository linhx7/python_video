from moviepy.editor import *
audio = AudioFileClip("video.mp4")#here i'm using the audio of the original video but if you have custom audio pass it here
audio = afx.audio_loop(audio, duration=500) #you can use n=X too 
clip1 = VideoFileClip("video.mp4")
clip1 = vfx.loop(clip1, duration=500) #you can use n=X too 
clip1 = clip1.set_audio(audio)
clip1.write_videofile("movie.mp4")