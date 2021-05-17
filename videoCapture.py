 First python code that grabs a screen capture from videos in testVideos(user has to include this folder into project
# folder
# Used Idiot Developer's Youtube video as a guide. https://www.youtube.com/watch?v=SWGd2hX5p3U

# Importing all required libraries
# Import open system library
import os
# Importing openCV library into script, version 4.5.2
import cv2
# Import the globe library. Used for returning all file paths that match specific patterns
from glob import glob

# Importing numpy library
import numpy as np

# To create a directory, first check if it already exists. If not then create it with os.makedirs('my folder')
# EAFP (Easier to ask for forgiveness than permission). Assume file exists and use Try and except statement
def create_dir(path):
   try:
       if not os.path.exists(path):
           # recursive directory creation function
           os.makedirs(path)
   except pathError:
       print(f" Error: Directory exists already {path}")

def save_frame(video_path, save_dir):
   # gap=20
   # Extract name from video path and splits pathname into just name of .mp4 without .mp4 extension
   name = video_path

   # Folder where frames will be saved
   save_path = os.path.join(save_dir, name)

   # Creates directory
   create_dir(save_path)

   # Video capture function that will capture image using cv2 library. Specify video path inside function
   capture = cv2.VideoCapture(video_path)
   # specify counter variable for naming captures
   capture_counter = 0

   # specify variable of 24 frames
   framesPer_picture = 24
   # counter starts at 24 frames since 0 is handled by first if statement, frames after 0 are handled by else statement
   counter = 1


   # while True loop will loop indefinitely ( i.e while true == true)
   # ret means return
   while True:
       # Capture frame-by-frame
       # cap.read returns a bool(True/False).  If frame is read correctly, it will be True. So you can check end of..
       # the video by checking this return value.
       ret, frame = capture.read()

       # if cap.read returns False then we are at the end of the video.
       if ret == False:
           # Everything is done, release the capture
           capture.release()
           # Exits if loop and either goes into else statement.
           break
       #else.

       #Syntax: cv2.imwrite(filename, image)

       #Parameters:
       # filename: A string representing the file name.The filename must include image format like.jpg,.png, etc.
       # image: It is the image that is to be saved.
       # Return Value: It returns true if image is saved successfully.cv2.imwrite()

       # Conditions for saving a frame every second
       if capture_counter ==0:
           cv2.imwrite(f"{save_path}/{capture_counter}.png", frame)
       else:
           # captures picture every 24 frames
           if capture_counter == (framesPer_picture * counter):
               cv2.imwrite(f"{save_path}/{capture_counter}.png", frame)
               counter += 1
       capture_counter += 1

if __name__ == "__main__":
   video_path = glob("testVideos/*")
   save_dir = "save"

   # for loop that iterates through the sequence ( video_path) the items in sequence are assigned to path as loop runs.
   for path in video_path:
       # save a frame every second (24 frames/second)
       save_frame(path, save_dir)
