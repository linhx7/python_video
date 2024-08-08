from moviepy.editor import *
from moviepy.editor import ColorClip
import random

# Function to create a resized part of the video
def create_resized_part(video, start_time, end_time, index, resize):
    # Cut the video to the specified part
    part = video.subclip(start_time, end_time)
    
    # Create a text clip to overlay on the video part
    text = TextClip(f"Part {index}", fontsize=70, color='white')
    text = text.set_pos('center').set_duration(part.duration)
    
    # Overlay the text on the video part
    video_with_text = CompositeVideoClip([part, text])
    
    # Resize the video part randomly between 0.9 and 1.0
    # resize_factor = random.uniform(0.9, 1.0)
    resized_video = video_with_text.resize(resize)
    width, height = video.size
    height = int(width * 16 / 9)
    return resized_video

def create_composite_video(background_video, overlay_video):
    overlay_video_duration = overlay_video.duration
    print(f"Width: {width}, Height: {height}")
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
    
overlay_video = VideoFileClip("babi.mp4").subclip(5,20)
# Get the width and height
width, height = overlay_video.size
height = int(width * 16 / 9)


# Create a black color clip with the specified dimensions
background_video = ColorClip(size=(width, height), color=(0, 0, 0))
# Set the duration of the clip (e.g., 10 seconds)
background_video = background_video.set_duration(50)
# Save the final video
# final_video = create_composite_video(background_video, overlay_video)
# final_video.write_videofile("final_video444.mp4")

# Loop through each part, create and resize
duration_per_part = overlay_video.duration / 2
video_parts = []
for i in range(2):
    start_time = i * duration_per_part
    end_time = (i + 1) * duration_per_part
    resize = 1
    if i == 1:
        resize = 0.5
    resized_part = create_resized_part(overlay_video, start_time, end_time, i+1, resize)
    compo_part = create_composite_video(background_video, resized_part)
    video_parts.append(compo_part)
    resized_part.write_videofile("compo_part"+ str(i+1)+ ".mp4") 
# Concatenate all the resized video parts
overlay_video = concatenate_videoclips(video_parts)    
overlay_video.write_videofile("overlay3.mp4")   

# Save the clip to a file
background_video.write_videofile("black_video.mp4", fps=24)


# Save the final video
final_video.write_videofile("final_video.mp4")