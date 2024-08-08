from moviepy.editor import *
from moviepy.editor import ColorClip
import random
import os
import glob

# Specify the relative folder path
folder_path = '.\\in'

# Function to create a resized part of the video
def create_resized_part(video, start_time, end_time, index, size):
    # Cut the video to the specified part
    part = video.subclip(start_time, end_time)
    
    # Create a text clip to overlay on the video part
    # text = TextClip(f"Part {index}", fontsize=70, color='white')
    # text = text.set_pos('center').set_duration(part.duration)
    
    # Overlay the text on the video part
    # video_with_text = CompositeVideoClip([part, text])
    
    
    video_with_text = part
    resized_video = video_with_text.resize(size)
    width, height = video.size
    height = int(width * 16 / 9)
    return resized_video

def create_composite_video(background_video, overlay_video):
    overlay_video_duration = overlay_video.duration
    # print(f"Width: {width}, Height: {height}")
    # Specify the width and height
    # Repeat Video 2 until its length matches the length of Video 1
    repeated_clips = []
    current_duration = 0
    while current_duration < overlay_video_duration:
        clip_duration = min(background_video.duration, overlay_video_duration - current_duration)
        repeated_clips.append(background_video.subclip(0, clip_duration))
        current_duration += clip_duration

    # Concatenate repeated clips of Video 2
    background_video_repeated = concatenate_videoclips(repeated_clips)
    pos_x = (background_video.w - overlay_video.w) // 2
    pos_y = (background_video.h - overlay_video.h) // 2
    position = (pos_x, pos_y)

    # Set the position of the overlay video
    overlay_video = overlay_video.set_position(position)

    # Create a composite video clip
    final_video = CompositeVideoClip([background_video_repeated, overlay_video])
    return final_video

def repeat_background_clip(overlay_video_duration, background_video):
    repeated_clips = []
    current_duration = 0
    while current_duration < overlay_video_duration:
        clip_duration = min(background_video.duration, overlay_video_duration - current_duration)
        repeated_clips.append(background_video.subclip(0, clip_duration))
        current_duration += clip_duration

    # Concatenate repeated clips of Video 2
    background_video_repeated2 = concatenate_videoclips(repeated_clips)
    background_video_repeated = background_video_repeated2.without_audio()
    return background_video_repeated
   
def conver_video(infile, outile):   
    overlay_video = VideoFileClip(infile)
    # Get the width and height
    width, height = overlay_video.size
    height = int(width * 16 / 9)
    print(f"Width: {width}, Height: {height}")

    print("duration", overlay_video.duration)

    # background_video1 = VideoFileClip("bg1.mp4")
    # width1, height1 = background_video1.size
    # print(f"Width2: {width1}, Height2: {height1}")
    # background_video1 = background_video1.resize(width/width1)
    # background_video = repeat_background_clip(overlay_video.duration, background_video1)
    # background_video.write_videofile("z1_fit3.mp4")   

    # Create a black color clip with the specified dimensions
    background_video1 = ColorClip(size=(width, int(width * 16 / 9)), color=(0, 0, 0))
    # Set the duration of the clip (e.g., 10 seconds)
    background_video1 = background_video1.set_duration(5)
    background_video = repeat_background_clip(overlay_video.duration, background_video1)

    # Loop through each part, create and resize
    partnum = 100
    duration_per_part = overlay_video.duration / partnum
    video_parts = []
    default_size_min = 0.93
    default_size_max = 0.97
    default_size_step = 0.001
    size = default_size_min
    direction = 1
    for i in range(partnum):
        start_time = i * duration_per_part
        end_time = (i + 1) * duration_per_part
        size  += direction * default_size_step
        if(size > default_size_max or size < default_size_min):
            direction = direction * -1
        # print(size)
        resized_part = create_resized_part(overlay_video, start_time, end_time, i+1, size)
        background_video_sub = background_video.subclip(start_time, end_time)
        compo_part = create_composite_video(background_video_sub, resized_part)
        video_parts.append(compo_part)
        # compo_part.write_videofile("compo_part"+ str(i+1)+ ".mp4") 
    # Concatenate all the resized video parts
    overlay_video = concatenate_videoclips(video_parts)    
    overlay_video.write_videofile(outile)   

# conver_video("in/z1.mp4", "out/z1out.mp4")

# Specify the relative folder path
folder_path = '.\\in'
# Use glob to find all files in the folder
files = glob.glob(os.path.join(folder_path, '*'))
# Loop through and read each file
for file_path in files:
    filename = os.path.basename(file_path)
    inp = "in/" + filename
    outp = "out/" + filename
    conver_video(inp, outp)