import cv2
import numpy as np
import pyautogui

# Setting the screen resolution to record
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# Setting the output video filename
output_filename = "recorded.mp4"

# Setting the frames per second for the recording
fps = 30.0

# Defining the codec and creating video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

# Defining the recording duration in seconds
recording_duration = 10

# Starting the screen recording
for i in range(int(fps * recording_duration)):
    # Capturing the screen
    screen = pyautogui.screenshot()

    # Converting the screenshot to a numpy array and BGR format for OpenCV
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Frame to output the video
    out.write(frame)

# Release the VideoWriter
out.release()
