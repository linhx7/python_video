from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout

# Load the video file
video = VideoFileClip("bg1.mp4")

# Load the image with gradient
gradient_image = ImageClip("gradient.jpg").set_duration(video.duration)

# Set the position and transparency of the image
gradient_image = gradient_image.set_opacity(0.5)  # Adjust opacity as needed
gradient_image = gradient_image.resize(height=video.h)  # Resize to match video height

# Overlay the image on the video
final_video = CompositeVideoClip([video, gradient_image.set_position(("center", "center"))])

# Write the final video to a file
final_video.write_videofile("output_video.mp4", codec="libx264")