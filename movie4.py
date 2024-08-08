from moviepy.editor import *
from moviepy.editor import ColorClip


# Function to create a resized part of the video
def create_resized_part(video, start_time, end_time, index):
    # Cut the video to the specified part
    part = video.subclip(start_time, end_time)
    
    # Create a text clip to overlay on the video part
    text = mpe.TextClip(f"Part {index}", fontsize=70, color='white')
    text = text.set_pos('center').set_duration(part.duration)
    
    # Overlay the text on the video part
    video_with_text = mpe.CompositeVideoClip([part, text])
    
    # Resize the video part randomly between 0.9 and 1.0
    resize_factor = random.uniform(0.9, 1.0)
    resized_video = video_with_text.resize(resize_factor)
    
    return resized_video

overlay_video = VideoFileClip("babi.mp4").subclip(5,20)
# Get the width and height
width, height = overlay_video.size

print(f"Width: {width}, Height: {height}")
# Specify the width and height

height = int(width * 16 / 9)

# Create a black color clip with the specified dimensions
background_video = ColorClip(size=(width, height), color=(0, 0, 0))

# Set the duration of the clip (e.g., 10 seconds)
background_video = background_video.set_duration(50)

# Save the clip to a file
background_video.write_videofile("black_video.mp4", fps=24)
overlay_video_duration = overlay_video.duration

# Repeat Video 2 until its length matches the length of Video 1
repeated_clips = []
current_duration = 0

while current_duration < overlay_video_duration:
    clip_duration = min(background_video.duration, overlay_video_duration - current_duration)
    repeated_clips.append(background_video.subclip(0, clip_duration))
    current_duration += clip_duration

# Concatenate repeated clips of Video 2
background_video_repeated = concatenate_videoclips(repeated_clips)

duration_per_part = overlay_video.duration / 10


overlay_video = overlay_video.rotate(0)
overlay_video = overlay_video.resize(0.9)
for(i =0 ; i< 10; i++)
pos_x = (background_video.w - overlay_video.w) // 2
pos_y = (background_video.h - overlay_video.h) // 2
position = (pos_x, pos_y)

# Set the position of the overlay video
overlay_video = overlay_video.set_position(position)

# Create a composite video clip
final_video = CompositeVideoClip([background_video_repeated, overlay_video])

# Save the final video
final_video.write_videofile("final_video.mp4")