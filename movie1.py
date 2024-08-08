from moviepy.editor import *
from moviepy.editor import ColorClip
overlay_video = VideoFileClip("babi.mp4").subclip(5,15)
# Get the width and height
width, height = overlay_video.size

print(f"Width: {width}, Height: {height}")
# Specify the width and height
width = 1280
height = int(width * 16 / 9)

# Create a black color clip with the specified dimensions
background_video = ColorClip(size=(width, height), color=(0, 0, 0))

# Set the duration of the clip (e.g., 10 seconds)
background_video = background_video.set_duration(10)

# Save the clip to a file
background_video.write_videofile("black_video.mp4", fps=24)

# Make the text. Many more options are available.
# txt_clip = ( TextClip("babilala",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )
# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("babi_exp.mp4",fps=25) # Many options...
# video_with_text = CompositeVideoClip([black_clip, video])
# video_with_text.write_videofile("final_video.mp4")


# Calculate the position to center the overlay video
# Centering it horizontally and vertically
overlay_video = overlay_video.rotate(0)

overlay_video = overlay_video.resize(0.9)
pos_x = (background_video.w - overlay_video.w) // 2
pos_y = (background_video.h - overlay_video.h) // 2
position = (pos_x, pos_y)

# Set the position of the overlay video
overlay_video = overlay_video.set_position(position)

# Create a composite video clip
final_video = CompositeVideoClip([background_video, overlay_video])

# Save the final video
final_video.write_videofile("final_video.mp4")