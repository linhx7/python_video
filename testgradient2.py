from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, TextClip, concatenate_videoclips

# Load the video file
video = VideoFileClip("bg1.mp4")

# Extract the first frame as an image
first_frame = video.get_frame(0)

# Create an ImageClip from the first frame
first_frame_clip = ImageClip(first_frame).set_duration(1)  # Display for 1 second

# Load the gradient image and resize it to match the video size
gradient_image = ImageClip("gradient.jpg").set_duration(1)
gradient_image = gradient_image.resize(height=video.h).set_opacity(0.5)

# Create a text clip
text = TextClip("Hot Hot Hot", fontsize=70, color='white').set_duration(1)
text = text.set_position('center')

# Composite the first frame, gradient overlay, and text together
composite = CompositeVideoClip([first_frame_clip, gradient_image.set_position(("center", "center")), text])

# Create the remainder of the original video, skipping the first second
remainder = video.subclip(1)  # Start the video from 1 second onward

# Concatenate the composite video with the remainder of the original video
final_video = concatenate_videoclips([composite, remainder])

# Write the final video to a file
final_video.write_videofile("final_output_video.mp4", codec="libx264")
